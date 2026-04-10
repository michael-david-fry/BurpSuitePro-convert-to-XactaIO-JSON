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
import logging
import configparser
import xml.etree.ElementTree as ET
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

def parse_burp_issues(root: ET.Element) -> List[Dict]:
    results = []

    for issue in root.findall(".//issue"):
        name = text_or_none(issue.find("name"))
        severity = text_or_none(issue.find("severity"))
        confidence = text_or_none(issue.find("confidence"))
        background = text_or_none(issue.find("issueBackground")) or name
        detail = text_or_none(issue.find("issueDetail"))
        host = text_or_none(issue.find("host"))
        path = text_or_none(issue.find("path"))
        cwe_id = text_or_none(issue.find("cweid"))
        vendor_id = infer_vendor_id(issue, name, host, path)
        port = parse_port_from_host_or_path(host, path)
        protocol = parse_protocol_from_host(host)
        test_data = build_test_data(host, path)

        notes = []
        if host:
            notes.append(f"Host: {host}")
        if path:
            notes.append(f"Path: {path}")
        if confidence:
            notes.append(f"Confidence: {confidence}")
        if detail:
            notes.append(detail)

        result_data = []
        if severity:
            result_data.append(f"Severity: {severity}")
        if confidence:
            result_data.append(f"Confidence: {confidence}")

        entry = {
            "vendorId": vendor_id,
            "testName": name,
            "description": background,
            "notes": "\n".join(notes),
            "result": scanner_result_from_severity(severity),
            "rawResult": "Fail",
            "riskFactor": map_severity(severity),
            "scanRiskFactor": map_severity(severity),
            "runTime": int(time.time() * 1000),
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

        test_results = parse_burp_issues(root)

        asset = [{
            "hostName": app_name,
            "dataSource": DATA_SOURCE_NAME,
            "scanDate": int(time.time() * 1000),
            "testResults": test_results
        }]

        if scanner_version:
            asset[0]["scannerVersion"] = scanner_version
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
