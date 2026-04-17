# XML to JSON Conversion Chart (Burp Suite XML ➜ Xacta JSON)

This chart documents the **current rendered output schema** produced by `burp_xml_to_xacta_json.py` after sanitization in `render_xacta_payload()`.

## Current rendered output shape

```json
{
  "assets": [
    {
      "hostName": "<normalized-lowercase-hostname>",
      "scanDate": "<ISO-8601>",
      "dataSource": "Burp Suite Professional",
      "systemName": "<optional>",
      "scannerVersion": "<optional>",
      "testResults": [
        {
          "vendorId": "<string>",
          "testName": "<string>",
          "description": "<string>",
          "result": "Pass|N/A|Fail",
          "rawResult": "Pass|N/A|Fail",
          "protocol": "HTTP|HTTPS|..."
        }
      ]
    }
  ]
}
```

## XML ➜ Rendered JSON mapping (exact)

| Burp XML source | Rendered Xacta JSON target | Transformation / logic |
|---|---|---|
| Root `<issues>` | Validation gate | Root tag **must** be `issues`, and at least one `<issue>` must exist. |
| `<issue><name>` | `assets[].testResults[].testName` | Trimmed text. Required in parser for result inclusion. |
| `<issue><type>` (preferred), else `<serialNumber>`, else `name|host|path` | `assets[].testResults[].vendorId` | First available source in that priority order. Required with `testName` for inclusion. |
| `<issue><severity>` | `assets[].testResults[].result` | If value is `pass` or `n/a` (case-insensitive): title-cased (`Pass` / `N/A`), otherwise `Fail`. |
| `<issue><severity>` | `assets[].testResults[].rawResult` | Same logic as `result`. |
| `<issue><issueBackground>`, `<issue><issueDetail>`, `<issue><remediationBackground>`, `<issue><remediationDetail>` | `assets[].testResults[].description` | Concatenated with blank lines; remediation lines are prefixed with labels. |
| `<issue><host>` (URL scheme) | `assets[].testResults[].protocol` | Parsed scheme uppercased (e.g., `http`→`HTTP`). Omitted if unavailable. |
| Config: `APPLICATION_NAME` | `assets[].hostName` | Used as hostName seed, then normalized to lowercase hostname in renderer. |
| `<issues exportTime="...">` | `assets[].scanDate` | Parsed to ISO-8601 string. Must be valid ISO-8601 after render validation. |
| Constant | `assets[].dataSource` | Always `Burp Suite Professional`. |
| Config: `SYSTEM_NAME` | `assets[].systemName` | Included when configured. |
| Config: `SCANNER_VERSION` else `<issues burpVersion="...">` | `assets[].scannerVersion` | Included when available. |

## Important rendered-schema constraints

Only the following **asset** fields survive rendering:

- `hostName`
- `scanDate`
- `dataSource`
- `systemName`
- `scannerVersion`
- `netAdapters`
- `softwares`
- `testResults`

Only the following **testResults** fields survive rendering:

- `testName`
- `description`
- `notes` *(explicitly removed right before output)*
- `result`
- `rawResult`
- `protocol`
- `vendorId`

### Fields computed earlier but not present in final rendered output

The parser computes additional fields, but they are dropped by render allowlists and note stripping:

- `riskFactor`, `scanRiskFactor`
- `runTime`
- `scannedWithCredentialsFlag`, `errorRunningTestFlag`
- `resultData`
- `testData`
- `port`
- `contents`
- `notes` (removed intentionally)

## Practical implications

- The final payload is intentionally compact and strict.
- Evidence-heavy metadata (including audit blocks and raw request/response in `notes`) is **not** present in the rendered JSON file.
- If downstream consumers require dropped fields, update `ALLOWED_TEST_RESULT_FIELDS` and renderer behavior.
