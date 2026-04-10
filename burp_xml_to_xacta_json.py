#!/usr/bin/env python3
"""
Burp Suite XML -> Xacta JSON Converter

Follows the Telos "Converting to External Data to Xacta JSON Using Python (v4.0)"
pattern by using config.ini for input/output configuration.

Purpose:
- Convert Burp Suite XML output into Xacta® JSON
- Intended for FedRAMP RA-5 / CA-7 DAST evidence
- NOT SCAP, NOT OpenSCAP, NOT compliance automation
"""

import os
import sys
import json
import time
import hashlib
import logging
import configparser
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse
from typing import List, Dict, Optional

# Optional dependency
try:
    from jsonschema import validate
    from jsonschema.exceptions import ValidationError
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False

# -----------------------------
# Logging (simple, PDF-aligned)
# -----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# -----------------------------
# Constants
# -----------------------------

DATA_SOURCE_NAME = "Burp Suite Professional"

SEVERITY_MAP = {
    "High": "High",
    "Medium": "Moderate",
    "Low": "Low",
    "Information": "Low"
}

REQUIRED_ROOT_TAG = "issues"
REQUIRED_ISSUE_FIELDS = ["name", "severity"]

# -----------------------------
# Minimal Xacta JSON schema
# -----------------------------

XACTA_JSON_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["hostName", "dataSource", "scanDate", "testResults"]
    }
}

# -----------------------------
# Helpers
# -----------------------------

def text_or_none(elem: Optional[ET.Element]) -> Optional[str]:
    if elem is None or elem.text is None:
        return None
    return elem.text.strip()

def map_severity(severity: Optional[str]) -> str:
    return SEVERITY_MAP.get(severity, "Low")

def scanner_result_from_severity(severity: Optional[str]) -> str:
    if severity and severity.strip().lower() in ("pass", "n/a"):
        return severity.strip().title()
    return "Fail"

def parse_port_from_host_or_path(host: Optional[str], path: Optional[str]) -> Optional[int]:
    for value in (host, path):
        if not value:
            continue
        candidate = value.strip()
        if "://" not in candidate:
            candidate = f"//{candidate}"
        parsed = urlparse(candidate)
        try:
            if parsed.port is not None:
                return parsed.port
        except ValueError:
            continue
    return None

def parse_protocol_from_host(host: Optional[str]) -> Optional[str]:
    if not host:
        return None
    parsed = urlparse(host.strip())
    if parsed.scheme:
        return parsed.scheme.upper()
    return None

def infer_vendor_id(issue: ET.Element, name: Optional[str], host: Optional[str], path: Optional[str]) -> Optional[str]:
    issue_type = text_or_none(issue.find("type"))
    if issue_type:
        return issue_type

    serial_number = text_or_none(issue.find("serialNumber"))
    if serial_number:
        return serial_number

    if name:
        return f"{name}|{host or ''}|{path or ''}"

    return None

def build_test_data(host: Optional[str], path: Optional[str]) -> Optional[str]:
    if host and path:
        if host.endswith("/") and path.startswith("/"):
            return f"{host[:-1]}{path}"
        if (not host.endswith("/")) and (not path.startswith("/")):
            return f"{host}/{path}"
        return f"{host}{path}"
    if host:
        return f"host={host}"
    if path:
        return f"path={path}"
    return None

def parse_export_time_to_epoch_ms(export_time: Optional[str]) -> Optional[int]:
    if not export_time:
        return None
    text = export_time.strip()
    try:
        dt = parsedate_to_datetime(text)
        return int(dt.timestamp() * 1000)
    except Exception:
        pass
    for fmt in ("%a %b %d %H:%M:%S %Z %Y", "%a %b %d %H:%M:%S %Y"):
        try:
            dt = datetime.strptime(text, fmt)
            return int(dt.timestamp() * 1000)
        except ValueError:
            continue
    return None

def extract_request_response(issue: ET.Element) -> Dict[str, Optional[str]]:
    request = None
    response = None
    http_method = None
    response_redirected = None
    requestresponse = issue.find("requestresponse")
    if requestresponse is not None:
        request_elem = requestresponse.find("request")
        response_elem = requestresponse.find("response")
        redirected_elem = requestresponse.find("responseRedirected")
        if request_elem is not None:
            request = (request_elem.text or "").strip() or None
            http_method = request_elem.attrib.get("method")
        if response_elem is not None:
            response = (response_elem.text or "").strip() or None
        if redirected_elem is not None:
            response_redirected = (redirected_elem.text or "").strip() or None
    return {
        "request": request,
        "response": response,
        "http_method": http_method,
        "response_redirected": response_redirected
    }

def extract_asset_ip_from_host(host: Optional[str]) -> Optional[str]:
    if not host:
        return None
    candidate = host.strip()
    if "://" not in candidate:
        candidate = f"//{candidate}"
    parsed = urlparse(candidate)
    host_name = parsed.hostname
    if not host_name:
        return None
    octets = host_name.split(".")
    if len(octets) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in octets):
        return host_name
    return None

def build_audit_source_record(
    issue: ET.Element,
    scanner_source: str,
    scanner_version: Optional[str],
    scan_date_value: Optional[str]
) -> Dict[str, str]:
    host = text_or_none(issue.find("host"))
    path = text_or_none(issue.find("path"))
    severity = text_or_none(issue.find("severity"))
    confidence = text_or_none(issue.find("confidence"))
    issue_background = text_or_none(issue.find("issueBackground"))
    issue_detail = text_or_none(issue.find("issueDetail"))
    remediation_background = text_or_none(issue.find("remediationBackground"))
    remediation_detail = text_or_none(issue.find("remediationDetail"))
    references = text_or_none(issue.find("references"))
    vulnerability_classifications = text_or_none(issue.find("vulnerabilityClassifications"))
    location = text_or_none(issue.find("location"))
    source_type = text_or_none(issue.find("type"))
    serial_number = text_or_none(issue.find("serialNumber"))
    static_analysis = text_or_none(issue.find("staticAnalysis"))
    request_response_data = extract_request_response(issue)

    weakness_parts = []
    cwe_id = text_or_none(issue.find("cweid"))
    if vulnerability_classifications:
        weakness_parts.append(vulnerability_classifications)
    if cwe_id:
        weakness_parts.append(f"CWE-{cwe_id}")

    return {
        "External ID": serial_number or source_type or "",
        "Title": text_or_none(issue.find("name")) or "",
        "Source Type": source_type or "",
        "Severity": severity or "",
        "Scanner Severity (Original)": severity or "",
        "Scanner Confidence": confidence or "",
        "Asset Hostname": host or "",
        "Asset IP Address": extract_asset_ip_from_host(host) or "",
        "Affected Resource": path or "",
        "Finding Location": location or "",
        "Description": issue_background or "",
        "Technical Details": issue_detail or "",
        "Remediation Rationale": remediation_background or "",
        "Recommended Remediation": remediation_detail or "",
        "References": references or "",
        "Weakness Classification": " | ".join(weakness_parts),
        "Evidence Request": request_response_data["request"] or "",
        "Evidence Response": request_response_data["response"] or "",
        "HTTP Method": request_response_data["http_method"] or "",
        "Scan Date": scan_date_value or "",
        "Scanner Source": scanner_source or "",
        "Evidence Hash": "",
        "Scanner Version": scanner_version or "",
        "Scan Type": static_analysis or ""
    }

def append_audit_block(notes_text: str, audit_record: Dict[str, str]) -> str:
    serialized = json.dumps(audit_record, separators=(",", ":"), ensure_ascii=False)
    block = (
        "[AUDIT_SOURCE_BURP_V1_BEGIN]\n"
        f"{serialized}\n"
        "[AUDIT_SOURCE_BURP_V1_END]"
    )
    if notes_text:
        return f"{notes_text}\n\n{block}"
    return block

def evidence_hash_from_record(audit_record: Dict[str, str]) -> str:
    serialized = json.dumps(audit_record, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

# -----------------------------
# Burp XML validation
# -----------------------------

def validate_burp_xml_structure(root: ET.Element) -> None:
    if root.tag != REQUIRED_ROOT_TAG:
        raise RuntimeError(
            f"Expected <{REQUIRED_ROOT_TAG}> root, found <{root.tag}>"
        )

    issues = root.findall(".//issue")
    if not issues:
        raise RuntimeError("No <issue> elements found in Burp XML")

    for idx, issue in enumerate(issues, start=1):
        for field in REQUIRED_ISSUE_FIELDS:
            if issue.find(field) is None:
                raise RuntimeError(
                    f"Issue #{idx} missing required <{field}> element"
                )

# -----------------------------
# Parse Burp issues
# -----------------------------

def parse_burp_issues(
    root: ET.Element,
    scanner_source: str,
    scanner_version: Optional[str],
    scan_date_epoch_ms: int,
    scan_date_value: Optional[str]
) -> List[Dict]:
    results = []

    for issue in root.findall(".//issue"):
        name = text_or_none(issue.find("name"))
        severity = text_or_none(issue.find("severity"))
        confidence = text_or_none(issue.find("confidence"))
        background = text_or_none(issue.find("issueBackground")) or name
        detail = text_or_none(issue.find("issueDetail"))
        location = text_or_none(issue.find("location"))
        remediation_background = text_or_none(issue.find("remediationBackground"))
        remediation_detail = text_or_none(issue.find("remediationDetail"))
        references = text_or_none(issue.find("references"))
        vulnerability_classifications = text_or_none(issue.find("vulnerabilityClassifications"))
        host = text_or_none(issue.find("host"))
        path = text_or_none(issue.find("path"))
        cwe_id = text_or_none(issue.find("cweid"))
        vendor_id = infer_vendor_id(issue, name, host, path)
        port = parse_port_from_host_or_path(host, path)
        protocol = parse_protocol_from_host(host)
        test_data = build_test_data(host, path)
        request_response_data = extract_request_response(issue)
        asset_ip = extract_asset_ip_from_host(host)

        notes = []
        if host:
            notes.append(f"Host: {host}")
        if asset_ip:
            notes.append(f"Asset IP Address: {asset_ip}")
        if path:
            notes.append(f"Path: {path}")
        if location:
            notes.append(f"Finding Location: {location}")
        if confidence:
            notes.append(f"Confidence: {confidence}")
        if references:
            notes.append(f"References: {references}")
        if remediation_background:
            notes.append(f"Remediation Rationale: {remediation_background}")
        if remediation_detail:
            notes.append(f"Recommended Remediation: {remediation_detail}")
        if request_response_data["response_redirected"]:
            notes.append(f"Response Redirected: {request_response_data['response_redirected']}")
        if detail:
            notes.append(detail)

        result_data = []
        source_type = text_or_none(issue.find("type"))
        serial_number = text_or_none(issue.find("serialNumber"))
        result_data.append(f"Source Type: {source_type or ''}")
        result_data.append(f"External ID: {serial_number or source_type or ''}")
        if severity:
            result_data.append(f"Severity: {severity}")
        if confidence:
            result_data.append(f"Confidence: {confidence}")
        if request_response_data["http_method"]:
            result_data.append(f"HTTP Method: {request_response_data['http_method']}")
        if scan_date_value:
            result_data.append(f"Scan Date: {scan_date_value}")
        result_data.append(f"Scanner Source: {scanner_source}")
        if scanner_version:
            result_data.append(f"Scanner Version: {scanner_version}")

        if request_response_data["http_method"]:
            method = request_response_data["http_method"]
            if test_data:
                test_data = f"{method} {test_data}"
            else:
                test_data = f"method={method}"

        description_parts = [p for p in (background, detail) if p]
        if remediation_background:
            description_parts.append(f"Remediation Rationale: {remediation_background}")
        if remediation_detail:
            description_parts.append(f"Recommended Remediation: {remediation_detail}")
        description = "\n\n".join(description_parts) if description_parts else None

        audit_record = build_audit_source_record(
            issue=issue,
            scanner_source=scanner_source,
            scanner_version=scanner_version,
            scan_date_value=scan_date_value
        )
        audit_record["Evidence Hash"] = evidence_hash_from_record(audit_record)

        entry = {
            "vendorId": vendor_id,
            "testName": name,
            "description": description or background,
            "notes": append_audit_block("\n".join(notes), audit_record),
            "result": scanner_result_from_severity(severity),
            "rawResult": scanner_result_from_severity(severity),
            "riskFactor": map_severity(severity),
            "scanRiskFactor": map_severity(severity),
            "runTime": scan_date_epoch_ms,
            "scannedWithCredentialsFlag": False,
            "errorRunningTestFlag": False
        }

        if result_data:
            entry["resultData"] = "; ".join(result_data)
        if test_data:
            entry["testData"] = test_data
        if protocol:
            entry["protocol"] = protocol
        if port is not None:
            entry["port"] = port
        if cwe_id:
            entry["contents"] = [
                {"name": f"CWE-{cwe_id}", "type": "CWE"}
            ]
        if vulnerability_classifications:
            entry.setdefault("contents", []).append(
                {"name": vulnerability_classifications, "type": "CWE"}
            )

        # vendorId and testName are core identifiers for test results
        if entry["vendorId"] and entry["testName"]:
            results.append(entry)
        else:
            logging.warning("Skipping issue with missing vendorId or testName")

    return results

# -----------------------------
# Xacta JSON validation
# -----------------------------

def validate_xacta_json(data: List[Dict]) -> None:
    if not JSONSCHEMA_AVAILABLE:
        logging.warning("jsonschema not installed; skipping Xacta JSON validation")
        return

    validate(instance=data, schema=XACTA_JSON_SCHEMA)
    logging.info("Xacta JSON schema validation passed")

# -----------------------------
# Main (PDF-style execution)
# -----------------------------

def main() -> None:
    config = configparser.ConfigParser()
    config.read("config.ini")

    if "BURP-IOJSON" not in config:
        logging.error("Missing [BURP-IOJSON] section in config.ini")
        sys.exit(1)

    input_dir = config["BURP-IOJSON"].get("INPUT_FOLDER")
    output_dir = config["BURP-IOJSON"].get("OUTPUT_FOLDER")
    app_name = config["BURP-IOJSON"].get("APPLICATION_NAME")
    scanner_version = config["BURP-IOJSON"].get("SCANNER_VERSION")
    system_name = config["BURP-IOJSON"].get("SYSTEM_NAME")

    if not input_dir or not output_dir or not app_name:
        logging.error("config.ini missing required values")
        sys.exit(1)

    if not os.path.isdir(input_dir):
        logging.error("Input folder does not exist: %s", input_dir)
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(".xml"):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(
            output_dir,
            filename.replace(".xml", "-xacta.json")
        )

        logging.info("Processing %s", filename)

        try:
            tree = ET.parse(input_path)
            root = tree.getroot()
            validate_burp_xml_structure(root)
        except Exception as e:
            logging.error("Skipping %s: %s", filename, e)
            continue

        scan_date_value = root.attrib.get("exportTime")
        scan_date_epoch_ms = parse_export_time_to_epoch_ms(scan_date_value) or int(time.time() * 1000)
        effective_scanner_version = scanner_version or root.attrib.get("burpVersion")

        test_results = parse_burp_issues(
            root=root,
            scanner_source=DATA_SOURCE_NAME,
            scanner_version=effective_scanner_version,
            scan_date_epoch_ms=scan_date_epoch_ms,
            scan_date_value=scan_date_value
        )

        asset = [{
            "hostName": app_name,
            "dataSource": DATA_SOURCE_NAME,
            "scanDate": scan_date_epoch_ms,
            "testResults": test_results
        }]

        if effective_scanner_version:
            asset[0]["scannerVersion"] = effective_scanner_version
        if system_name:
            asset[0]["systemName"] = system_name

        try:
            validate_xacta_json(asset)
        except Exception as e:
            logging.error("Validation failed for %s: %s", filename, e)
            continue

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(asset, f, indent=2)

        logging.info("Wrote %s", output_path)

if __name__ == "__main__":
    main()
