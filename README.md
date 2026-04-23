# Burp XML to Xacta JSON (v3)

This repo includes a **v3 converter** that transforms Burp Suite XML findings into Xacta-compatible JSON while matching the field **structure and ordering** shown in:

- `Xacta io Documentation/XIO JSON Template.json`

## What v3 changes

Compared to `burp_xml_to_xacta_json_v2.py`, v3:

- Produces a **top-level JSON array** of assets (`[ ... ]`) to match the documentation template shape.
- Applies deterministic key ordering for:
  - asset fields
  - `testResults` fields
- Keeps v2 behavior for:
  - grouping findings by normalized host
  - extracting IPs for `netAdapters`
  - embedding audit/source metadata in `notes`
  - sanitizing/truncating request/response snippets

## Files

- `burp_xml_to_xacta_json_v3.py` — v3 converter script
- `config.ini` — runtime input/output/application configuration
- `input/` — place Burp XML exports here
- `output/` — generated Xacta JSON files

## Configuration

Edit `config.ini` section `[BURP-IOJSON]`:

- `INPUT_FOLDER` — folder containing Burp XML files
- `OUTPUT_FOLDER` — folder for generated JSON files
- `APPLICATION_NAME` — logical system/app name used in output
- `SCANNER_VERSION` — optional override
- `SYSTEM_NAME` — optional output `systemName`

## Usage

Run:

```bash
python3 burp_xml_to_xacta_json_v3.py
```

The script will:

1. load `config.ini`
2. parse all `.xml` files in `INPUT_FOLDER`
3. write `*-xacta.json` files into `OUTPUT_FOLDER`

## Output format notes

- v3 output shape is a JSON array of assets.
- Each asset contains template-ordered fields (where values exist), including `dataSource`, `hostName`, `scanDate`, `testResults`, `softwares`, and `netAdapters`.
- Each test result contains template-ordered vulnerability fields such as `vendorId`, `testName`, `notes`, `solution`, `description`, `result`, `rawResult`, `riskFactor`, `severity`, `resultData`, and `testData`.

## Quick validation

After running, inspect one output file:

```bash
python3 -m json.tool output/<file>-xacta.json | head
```

You should see the JSON begin with `[` (array), not an object wrapper.
