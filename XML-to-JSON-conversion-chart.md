# XML to JSON Conversion Chart (Burp Suite XML ➜ Xacta JSON)

This chart documents the **current v3 output schema** produced by `burp_xml_to_xacta_json_v3.py`.

## Current rendered output shape (v3)

```json
[
  {
    "dataSource": "Burp Suite Professional",
    "hostName": "<normalized-lowercase-hostname>",
    "scanDate": "<ISO-8601>",
    "systemName": "<optional>",
    "scannerVersion": "<optional>",
    "testResults": [
      {
        "vendorId": "<string>",
        "testName": "<string>",
        "notes": "<string>",
        "solution": "<optional-string>",
        "description": "<string>",
        "result": "Pass|N/A|Fail",
        "rawResult": "Pass|N/A|Fail",
        "contents": [
          { "name": "CWE-79", "type": "CWE" }
        ],
        "port": 443,
        "protocol": "HTTP|HTTPS|...",
        "runTime": 1719446400000,
        "scannedWithCredentialsFlag": false,
        "errorRunningTestFlag": false,
        "riskFactor": "Low|Moderate|High",
        "severity": "Information|Low|Medium|High",
        "resultData": {
          "Source Type": "<string>",
          "External ID": "<string>",
          "Severity": "<string>",
          "Confidence": "<string>",
          "HTTP Method": "<string>",
          "Scan Date": "<string>",
          "Scanner Source": "Burp Suite Professional",
          "Scanner Version": "<optional-string>"
        },
        "testData": "<string>"
      }
    ],
    "netAdapters": [
      { "ipAddress": "192.0.2.10" }
    ]
  }
]
```

## XML ➜ Rendered JSON mapping (exact v3)

| Burp XML source | Rendered Xacta JSON target | Transformation / logic |
|---|---|---|
| Root `<issues>` | Validation gate | Root tag **must** be `issues`, and at least one `<issue>` must exist. |
| `<issue><host>` | `asset.hostName` grouping key | Host is normalized with URL parsing (`scheme/port/path removed`), lowercased, trailing `.` stripped. If missing/unparseable, grouped as `unknown.local`. |
| `<issue><name>` | `testResults[].testName` | Trimmed text. Required (with `vendorId`) for inclusion. |
| `<issue><type>` (preferred), else `<serialNumber>`, else `name|host|path` | `testResults[].vendorId` | First available source in that priority order. |
| `<issue><severity>` | `testResults[].result` + `rawResult` | If severity is `pass` or `n/a` (case-insensitive), output title-case; otherwise `Fail`. |
| `<issue><severity>` | `testResults[].riskFactor` | Mapped: `High→High`, `Medium→Moderate`, `Low→Low`, `Information→Low`; unknown defaults to `Low`. |
| `<issue><severity>` | `testResults[].severity` | Original Burp severity text (fallback `Information`). |
| `<issue><issueBackground>` + `<issue><issueDetail>` | `testResults[].description` | Combined with blank line separator when both exist. |
| `<issue><remediationBackground>` + `<issue><remediationDetail>` | `testResults[].solution` | Combined with blank line separator when present. |
| `<issue><host>` (URL scheme) | `testResults[].protocol` | Parsed scheme uppercased (`http`→`HTTP`). |
| `<issue><host>` + `<issue><path>` | `testResults[].port` | Port parsed from host/path URL if present. |
| `<issue><cweid>` and `<issue><vulnerabilityClassifications>` | `testResults[].contents[]` | Added as CWE-tagged content entries. |
| `<issue><host ip="...">` (preferred), else IP parsed from `<host>` | `asset.netAdapters[].ipAddress` | Unique per host group, sorted in output. |
| `<issue>` request/response metadata + finding text fields | `testResults[].notes` | Human-readable notes plus appended `[AUDIT_SOURCE_BURP_V1_*]` JSON block; snippets truncated/sanitized. |
| `<issue>` + scanner metadata | `testResults[].resultData` | Includes source identifiers and scan metadata key/value pairs. |
| `<issues exportTime="...">` | `asset.scanDate` + `testResults[].runTime` | ISO-8601 for `scanDate`; epoch-ms for `runTime` (fallback current time if parse fails). |
| Constant | `asset.dataSource` | Always `Burp Suite Professional`. |
| Config `SYSTEM_NAME` else `APPLICATION_NAME` | `asset.systemName` | Uses configured system name; falls back to application name. |
| Config `SCANNER_VERSION` else `<issues burpVersion="...">` | `asset.scannerVersion` | Included when available. |

## Host grouping and test result aggregation

- The converter creates **one asset per normalized hostName**.
- All issues mapped to that host are appended into that asset's `testResults` array.
- Duplicate asset host names are rejected at render time.

Implication:
- You get **multiple entries across different hosts**, and **multiple test results within each host entry**.

## Rendered-field ordering (v3)

Assets are emitted in this order when present:

- `dataSource`, `hostName`, `assetRole`, `ramSize`, `scanDate`, `scannerVersion`, `systemName`, `cpus`, `biosManufacturer`, `biosVersion`, `biosDate`, `osList`, `driveList`, `vendorInfo`, `systemModel`, `serial`, `poc`, `endpointData`, `cloudInfo`, `testResults`, `softwares`, `netAdapters`

Test results are emitted in this order when present:

- `vendorId`, `testName`, `notes`, `solution`, `description`, `result`, `rawResult`, `contents`, `port`, `protocol`, `runTime`, `firstSeen`, `scannedWithCredentialsFlag`, `errorRunningTestFlag`, `riskFactor`, `severity`, `catValue`, `cvssScore`, `cvssVersion`, `isTestNameTestIdentifier`, `resultData`, `testData`

## Import-relevant notes

- Top-level output is a **JSON array** (`[ ... ]`), not `{ "assets": [...] }`.
- `hostName` must be unique per asset after normalization.
- `scanDate` must remain valid ISO-8601 or rendering fails validation.
- If host parsing fails, findings collapse into `unknown.local`, which can merge otherwise unrelated findings.
