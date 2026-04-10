# XML to JSON Conversion Chart (Burp Suite XML ➜ Xacta JSON)

This chart documents how Burp Suite XML fields are transformed into Xacta-compatible JSON fields, plus **why** each mapping is used.

## Conversion reasoning summary

- The converter creates a JSON **array of assets**, where each asset has `hostName`, `dataSource`, `scanDate`, and `testResults`.
- Each Burp `<issue>` becomes one `testResults[]` entry.
- Severity values are normalized for Xacta-style risk language (`High`, `Moderate`, `Low`).
- Scanner-specific context (request/response, confidence, serial number, etc.) is preserved in `notes` using an audit block so source evidence is retained.

## XML ➜ JSON mapping chart

| Burp XML source | Xacta JSON target | Transformation / Logic | Reasoning |
|---|---|---|---|
| Root `<issues>` | Top-level JSON array | Validate root tag before processing. | Ensures the input is Burp issue export format and avoids converting invalid XML structures. |
| `<issue>` | `testResults[]` object | Each issue is iterated and converted to one result record. | Keeps one vulnerability finding per record for traceability and downstream filtering. |
| `<issue><name>` | `testResults[].testName` | Trimmed text; required field. | Preserves Burp's finding title as the primary human-readable identifier. |
| `<issue><severity>` | `testResults[].severity` | Map using: `High→High`, `Medium→Moderate`, `Low→Low`, `Information→Low`; fallback `Low`. | Normalizes scanner wording into Xacta-compatible risk levels. |
| `<issue><severity>` | `testResults[].scannerResult` | If severity text is `pass` or `n/a` (case-insensitive), set to `Pass`/`N/A`; otherwise `Fail`. | Keeps machine-friendly pass/fail status for compliance-style result handling. |
| `<issue><type>` (preferred), else `<serialNumber>`, else derived composite (`name|host|path`) | `testResults[].vendorId` | Use first available source in priority order. | Provides stable vendor/source identifier even when one field is missing. |
| `<issue><issueBackground>` + `<issue><issueDetail>` | `testResults[].description` | Concatenate descriptive fields where present. | Combines Burp explanation and issue-specific details into analyst-readable context. |
| `<issue><remediationBackground>` + `<issue><remediationDetail>` | `testResults[].recommendation` | Concatenate remediation fields where present. | Preserves both generic and instance-specific fix guidance in one destination field. |
| `<issue><host>` + `<issue><path>` | `testResults[].testData` | Build URL-like value; normalize slash joining. Fallback to `host=...` or `path=...` if only one exists. | Retains actionable target evidence used during the test. |
| `<issue><host>` | `testResults[].assetIp` (when possible) | Parse hostname from URL/host; emit only if it is a valid IPv4 address. | Prevents invalid/non-IP hostnames from being misclassified as IP assets. |
| `<issue><host>` | `testResults[].networkProtocol` | Parse URI scheme and uppercase (`http`→`HTTP`, `https`→`HTTPS`) when available. | Captures protocol metadata useful for routing and reporting. |
| `<issue><host>` or `<issue><path>` | `testResults[].port` | Parse explicit port from host or path URL when present. | Stores transport endpoint detail for correlation with infra data. |
| `<issue><requestresponse><request method="...">` | `testResults[].networkService` / notes audit fields | Capture HTTP method attribute if present. | Method (`GET`, `POST`, etc.) is often required for repro and triage. |
| `<issue><requestresponse><request>` and `<response>` | Notes audit block (`Raw Request`, `Raw Response`) | Preserve raw payloads as scanner evidence metadata. | Maintains forensic detail without overloading top-level semantic fields. |
| `<issue><confidence>` | Notes + audit block | Included as textual metadata. | Confidence helps prioritization and false-positive analysis. |
| `<issue><cweid>` and `<issue><vulnerabilityClassifications>` | Notes audit block / weakness context | Combine into weakness text where available. | Retains taxonomy evidence used for risk mapping and reporting standards. |
| `<issues exportTime="...">` | Asset `scanDate` (epoch ms) | Parse export timestamp formats; convert to epoch milliseconds. | Standardized numeric timestamp simplifies ingestion and time-based analytics. |
| Config / constant (`Burp Suite Professional`) | Asset `dataSource` | Fixed data source value. | Labels origin system for multi-scanner aggregation. |
| Derived grouping key (asset/host logic) | Asset object `hostName` | Findings grouped under generated host grouping label. | Produces Xacta asset-centric structure while preserving per-finding details in `testResults`. |

## Practical notes

- Unknown or missing optional XML fields are handled gracefully; converter uses fallbacks rather than failing where possible.
- Validation checks enforce minimum structure (required root tag and required issue fields) before output.
- Optional JSON schema validation can be run when `jsonschema` is installed.

## Example mini-mapping

```xml
<issue>
  <name>SQL injection</name>
  <severity>High</severity>
  <host>https://example.com:8443</host>
  <path>/search</path>
  <type>123456</type>
</issue>
```

```json
{
  "testName": "SQL injection",
  "severity": "High",
  "scannerResult": "Fail",
  "vendorId": "123456",
  "networkProtocol": "HTTPS",
  "port": 8443,
  "testData": "https://example.com:8443/search"
}
```

Reasoning: this keeps scanner-native identity (`type`), normalized risk (`severity`), and reproducible target context (`protocol`, `port`, `testData`) in one record.
