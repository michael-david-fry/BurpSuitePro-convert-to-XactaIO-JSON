# Auditable XML→JSON Conversion Logic Report (v3)

**Scope reviewed:** `burp_xml_to_xacta_json_v3.py`  
**Conversion direction:** Burp Suite XML (`<issues><issue>...`) → Xacta JSON array of assets (`[ { ... } ]`)  
**Execution mode for this report:** Static code inspection only (no runtime execution)

## 1) Control Objectives

1. **Structural validity of source XML** before mapping.
2. **Deterministic transformation** from XML fields to JSON fields.
3. **Data minimization/sanitization** for notes/evidence snippets.
4. **Post-transform payload validation** before write.
5. **Traceability/auditability** by embedding source metadata and evidence hash.

## 2) End-to-End Processing Flow

1. Read `config.ini` and required `[BURP-IOJSON]` keys (`INPUT_FOLDER`, `OUTPUT_FOLDER`, `APPLICATION_NAME`) (`main`, lines 747–763).
2. Iterate XML files in input directory (`main`, lines 771–779).
3. Parse XML via `ElementTree`; reject invalid structure (`validate_burp_xml_structure`, lines 480–493; call at 783–787).
4. Derive scan metadata from root attributes:
   - `exportTime` → epoch ms (`runTime`) and ISO-8601 (`scanDate`) (`791–794`, helpers `222–248`)
   - scanner version from config or `burpVersion` (`794`)
5. Parse issues and group by normalized host (`parse_burp_issues_by_host`, lines 500–659).
6. Build one asset per host group (`810–832`).
7. Render ordered/sanitized payload and enforce uniqueness/shape (`render_xacta_payload`, 670–732).
8. Optionally validate via `jsonschema` if installed (`735–740`).
9. Write JSON output (`845–848`).

## 3) Input Validation Logic (Preconditions)

### XML-level gates
- Root tag must be `issues` (`481–484`).
- Must contain at least one `<issue>` (`485–487`).
- Every issue must have `<name>` and `<severity>` elements (`488–493`).

### Config-level gates
- Missing config section or required values causes immediate exit (`751–763`).
- Missing input directory causes exit (`765–767`).

## 4) Canonical Mapping Logic (Field-by-Field)

### Asset-level mappings

- `dataSource` ← constant `"Burp Suite Professional"` (`56`, asset creation at `815`).
- `hostName` ← normalized `<issue><host>` hostname, grouped per host (`195–205`, `538–541`, asset at `814`).
- `scanDate` ← ISO-8601 from `<issues exportTime="...">` (`240–248`, `791`, `793`, asset at `816`).
- `scannerVersion` ← config `SCANNER_VERSION` override, else root `burpVersion` (`758`, `794`, `821–823`).
- `systemName` ← config `SYSTEM_NAME` or fallback `APPLICATION_NAME` (`759`, `795`, asset at `817`).
- `netAdapters[].ipAddress` ← unique/sorted IPs from `<host ip="...">` or host-text IP parse (`251–280`, `544–546`, `824–829`).
- `testResults` ← all mapped issues for that host (`818`).

### TestResult-level mappings

- `vendorId` ← `<type>` else `<serialNumber>` else `name|host|path` (`183–192`, use at `532`, set at `622`).
- `testName` ← `<name>` (`519`, `623`).
- `description` ← `<issueBackground>` + `<issueDetail>` joined (`522–524`, `600–603`, set at `624`).
- `solution` ← `<remediationBackground>` + `<remediationDetail>` joined if present (`525–527`, `604–610`, `635–636`).
- `result` / `rawResult` ← `"Pass"`/`"N/A"` only if severity text is pass-like, else `"Fail"` (`152–156`, `626–627`).
- `riskFactor` ← severity map `High→High`, `Medium→Moderate`, `Low→Low`, `Information→Low`, fallback `Low` (`58–63`, `148–149`, `628`).
- `severity` ← original `<severity>` or `"Information"` fallback (`520`, `629`).
- `runTime` ← epoch ms from export time (or current time fallback in main) (`222–237`, `792`, `630`).
- `protocol` ← URL scheme from host uppercased (`174–180`, `534`, `641–642`).
- `port` ← parsed from host/path URL if present (`158–171`, `533`, `643–644`).
- `contents`:
  - add CWE entry from `<cweid>` (`531`, `645–648`)
  - append vulnerability classifications blob from `<vulnerabilityClassifications>` as CWE-typed entry (`528`, `649–652`)
- `testData` ← synthesized host/path string; prefixed with HTTP method if available (`208–219`, `593–599`, `639–640`).
- `resultData` object includes source/severity/confidence/method/scan metadata (`575–591`, set at `637–638`).
- `notes`:
  - line-based assembled context (host/path/location/confidence/etc.) (`548–573`)
  - embeds audit JSON block (`459–468`, set at `625`).

## 5) Audit and Evidence Features

1. `build_audit_source_record` assembles a structured record from issue fields and scan metadata (`400–456`).
2. SHA-256 evidence hash computed over serialized audit record (`471–473`, applied at `619`).
3. Record embedded in `notes` between markers:
   - `[AUDIT_SOURCE_BURP_V1_BEGIN]`
   - `[AUDIT_SOURCE_BURP_V1_END]`
   (`134–135`, `459–468`).
4. `sanitize_notes_text` preserves audit block while normalizing notes and re-truncating snippet lines (`320–360`, invoked at `703–705`).

## 6) Post-Transform Integrity Controls

In `render_xacta_payload`:

- Enforces ordered keys via allowlist order arrays (`82–131`, `666–667`, `687`, `702`, `727`).
- Validates `hostName` is parseable and non-empty (`679–682`, `717–719`).
- Validates `scanDate` ISO-8601 (`683–685`, `724–725`, helper `363–370`).
- Ensures `testResults` is array if present (`691–695`).
- Enforces `dataSource` when `testResults` exists (`695–696`).
- Removes empty/null structures recursively (`283–306`, used at `705`, `713`).
- Rejects duplicate asset hostnames (`720–722`).
- Rejects empty final payload (`729–730`).

Optional schema validation:
- If `jsonschema` available, validates against minimal schema requiring array items with `dataSource`, `hostName`, `scanDate` (`68–80`, `735–740`).

## 7) Determinism & Reproducibility Notes

- Asset groups are iterated with `sorted(host_groups.items())` for deterministic asset ordering (`812`).
- IPs sorted before `netAdapters` emission (`828`).
- Field order is deterministic using explicit order lists (`82–131`).
- Non-deterministic fallback exists for `runTime` when `exportTime` cannot be parsed (`792` uses current time).

## 8) Error Handling Behavior

- File-level failures are logged and skipped, not fatal for whole batch (`787–789`, `841–843`).
- Invalid transformed asset/test content can be dropped or cause file skip depending on stage.
- Missing `vendorId` or `testName` causes issue skip with warning (`654–657`).

## 9) Known Logic Boundaries (for audit awareness)

1. Only the first `<requestresponse>` is read (`issue.find("requestresponse")`, `378`) even if multiple exist.
2. Base64-encoded request/response payloads are not decoded (text is used as-is; attributes read only for method) (`380–387`).
3. Unknown/unparseable host values collapse into `"unknown.local"` grouping key (`540–541`).
4. `riskFactor` mapping defaults unknown severities to `"Low"` (`149`).

## 10) Traceability Matrix (compact)

- **Source validation:** `validate_burp_xml_structure` (480–493)
- **Host grouping:** `normalize_hostname`, `parse_burp_issues_by_host` (195–205, 500–659)
- **Issue→TestResult mapping core:** (518–653, 621–652)
- **Audit block generation:** `build_audit_source_record`, `evidence_hash_from_record`, `append_audit_block` (400–473)
- **Sanitization/order enforcement:** `sanitize_notes_text`, `remove_empty_structures`, `ordered_subset`, `render_xacta_payload` (320–360, 283–306, 666–732)
- **Serialization/write:** `main` write block (845–848)
