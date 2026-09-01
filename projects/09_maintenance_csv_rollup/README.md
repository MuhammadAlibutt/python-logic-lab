# Project 09 — Maintenance CSV Roll-Up

**Timebox:** 2–3 hours  
**Skills:** CSV, fatal versus row errors, aggregation, sorting, CLI arguments, temporary-file tests

## Objective

Read a maintenance-event CSV, reject bad rows safely, aggregate valid records by equipment, and write a clean summary CSV. Do not use pandas.

Run:

```text
python project.py INPUT.csv OUTPUT.csv
```

Required input headers:

```text
equipment_id,fault_code,downtime_minutes,resolved
```

Extra headers are allowed. Missing required headers are a fatal file error.

## Row rules

- Equipment ID and fault code are non-empty, trimmed, and uppercased.
- Downtime is a whole integer of zero or more.
- Resolved is `yes` or `no`, case-insensitively.
- A completely blank row is ignored.
- Any other invalid row is skipped and counted.
- Duplicate valid rows are separate incidents.

## Output

```text
equipment_id,incident_count,total_downtime_minutes,unresolved_count
```

One row per equipment, sorted alphabetically.

Example input:

```csv
equipment_id,fault_code,downtime_minutes,resolved
CV-01,JAM,12,yes
CV-01,SENSOR,8,no
SC-02,MOTOR,30,yes
CV-01,JAM,bad,no
,NETWORK,4,yes
SC-02,JAM,5,no
```

Expected output:

```csv
equipment_id,incident_count,total_downtime_minutes,unresolved_count
CV-01,2,20,1
SC-02,2,35,1
```

Print:

```text
Processed: 6 | Valid: 4 | Skipped: 2 | Equipment: 2
```

## CLI/error requirements

- Require exactly input and output arguments.
- Missing/unreadable input → friendly error.
- Refuse when input and output resolve to the same file.
- Missing headers produce no misleading output.
- A valid run may replace an existing output.
- Expected errors do not show tracebacks.

## Tests to write

- Valid row conversion and normalisation
- Negative/decimal downtime and missing fields
- Invalid resolved values
- Required headers and harmless extra headers
- Incident, downtime, and unresolved totals
- Duplicate records
- Alphabetical equipment order
- Header-only and mixed-validity files
- Same input/output path
- Temporary-file workflow test

## Stretch

- Write skipped rows to a rejection CSV with reasons.
- Add totals by fault code or an unresolved-only filter.
- Preserve an existing output if processing fails unexpectedly.

## Definition of done

- You can explain the difference between a fatal file error and a skippable row error.
- Invalid rows are counted and never silently disappear.
- At least twelve tests pass.
- Output schema and ordering are exact.

Suggested commits:

```text
docs: define maintenance input and output
feat: validate maintenance rows
feat: aggregate equipment statistics
feat: add csv workflow and cli errors
test: cover files rows and totals
docs: record project 09 reflection
```

