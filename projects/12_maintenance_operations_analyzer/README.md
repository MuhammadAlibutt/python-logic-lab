# Project 12 — Maintenance Operations Analyzer

**Level:** Intermediate capstone

**Estimated time:** 10–15 focused hours

**Start after:** CS50P Object-Oriented Programming and Unit Tests

## Scenario

An airport maintenance team receives asset records, work orders, and free-text technician notes from different systems. Build a command-line application that validates those inputs, joins the related records, detects operational risks, and creates clear reports.

Use synthetic data only. Never commit real company records, names, IDs, costs, or operational details.

## What this project practises

- Breaking a larger problem into modules
- Regular expressions
- CSV, JSON, and text-file processing
- Exceptions and validation
- Dates and times
- Classes and object-oriented design
- Command-line arguments
- Unit and integration tests
- Deterministic reporting

## Required command

Your finished program should support a command similar to:

```text
python -m maintenance_analyzer analyze \
  --assets data/sample/assets.csv \
  --work-orders data/sample/work_orders.csv \
  --notes data/sample/technician_notes.txt \
  --config data/sample/config.json \
  --as-of "2026-09-01 00:00" \
  --output reports
```

Also support `--strict`:

- Without `--strict`, reject invalid rows, record the problems, and continue when safe.
- With `--strict`, stop when the first invalid record is found.

Use these exit codes:

- `0`: analysis completed and no records were rejected
- `1`: analysis completed, but one or more invalid records were skipped
- `2`: a fatal problem prevented analysis, such as a missing file or invalid configuration

## Input 1: `assets.csv`

Required columns:

| Column | Rule |
|---|---|
| `asset_id` | `BHS`, `GSE`, or `SEC`, followed by `-` and four digits; must be unique |
| `asset_type` | Non-blank text |
| `location` | Non-blank text |
| `criticality` | Integer from 1 to 5 |
| `commissioned_date` | Valid `YYYY-MM-DD` date |

Examples of valid IDs: `BHS-1001`, `GSE-2042`, `SEC-0107`.

## Input 2: `work_orders.csv`

Required columns:

| Column | Rule |
|---|---|
| `work_order_id` | `WO-` followed by six digits; must be unique |
| `asset_id` | Must exist in `assets.csv` |
| `opened_at` | Valid `YYYY-MM-DD HH:MM` timestamp |
| `responded_at` | Valid timestamp or blank |
| `closed_at` | Valid timestamp or blank |
| `priority` | `P1`, `P2`, `P3`, or `P4` |
| `status` | `OPEN`, `IN_PROGRESS`, or `CLOSED` |
| `fault_code` | `E` followed by three digits |
| `downtime_minutes` | Non-negative integer |
| `parts_cost` | Non-negative decimal value; use `Decimal`, not `float` |
| `summary` | Non-blank text |

Additional rules:

- `responded_at` cannot be earlier than `opened_at`.
- `closed_at` cannot be earlier than either `opened_at` or `responded_at`.
- A `CLOSED` work order must have `closed_at`.
- An `OPEN` or `IN_PROGRESS` work order must not have `closed_at`.

## Input 3: `technician_notes.txt`

Each non-blank line uses this format:

```text
[2026-08-03 10:05] WO-000101 BHS-1001 TECH=AK123 CODE=E042 DOWN=90m :: Belt obstruction cleared
```

Build one named-group regular expression that extracts:

- timestamp
- work-order ID
- asset ID
- technician ID
- fault code
- downtime minutes
- note text

Then cross-check each parsed note against its work order. Report a quality problem if:

- the line is malformed;
- the work order is unknown;
- its asset ID or fault code disagrees with the work order;
- its downtime differs from the work-order value;
- a valid work order has no matching technician note.

## Input 4: `config.json`

Required shape:

```json
{
  "sla_response_hours": {
    "P1": 1,
    "P2": 4,
    "P3": 12,
    "P4": 24
  },
  "repeat_window_days": 30,
  "repeat_threshold": 2
}
```

All values must be positive numbers or integers as appropriate, and all four priorities must be present.

## Required analyses

### 1. Overall metrics

Calculate at least:

- accepted and rejected record counts;
- work orders by status and priority;
- total downtime;
- total parts cost;
- median response time for responded work orders;
- five assets with the most downtime.

### 2. SLA performance

For each work order, compare response time with the limit for its priority.

- A response exactly on the boundary meets the SLA.
- For an unresponded work order, measure from `opened_at` to `--as-of`.
- Do not use the computer's current clock. Results must be repeatable for the same inputs and `--as-of` value.

Report totals and compliance percentages overall and by priority.

### 3. Repeat-fault detection

A repeat-fault group contains the same `asset_id` and `fault_code` at least `repeat_threshold` times inside an inclusive `repeat_window_days` period.

Report the asset, fault code, occurrence count, first date, last date, and related work-order IDs. Define and document how overlapping qualifying windows are grouped.

### 4. Asset attention score

For each asset, calculate:

```text
criticality
+ 5 for each open P1 work order
+ 3 for each open P2 work order
+ 2 for each other open work order
+ 2 for each repeat-fault group
+ min(5, whole hours of downtime)
```

Sort by score descending, then downtime descending, then asset ID ascending. Make every other report order deterministic too.

## Data-quality records

Represent every issue consistently with these fields:

- `severity`
- `source`
- `row_number`
- `record_id`
- `field`
- `message`

Choose a small documented set of severity values and use it consistently.

## Required output files

Write these files inside the directory supplied by `--output`:

1. `summary.json` — metrics, SLA results, repeat faults, and run metadata
2. `asset_report.csv` — one row per asset, including its attention score
3. `data_quality.csv` — every validation and cross-check problem
4. `report.md` — a concise report a maintenance manager could read

Your program may create the output directory if it does not exist. Re-running it with the same data should safely replace its own report files.

## Suggested structure

```text
projects/12_maintenance_operations_analyzer/
├── data/
│   └── sample/
│       ├── assets.csv
│       ├── work_orders.csv
│       ├── technician_notes.txt
│       └── config.json
├── src/
│   └── maintenance_analyzer/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py
│       ├── cli.py
│       ├── exceptions.py
│       ├── loaders.py
│       ├── models.py
│       ├── note_parser.py
│       └── reports.py
└── tests/
```

You can change the structure if you can explain why your design is clearer.

## Build it in milestones

1. Write `PLAN.md`, example inputs, and pseudocode.
2. Validate and load assets.
3. Validate and load work orders.
4. Parse and cross-check technician notes.
5. Implement overall and SLA metrics.
6. Implement repeat-fault detection and attention scores.
7. Produce all four reports.
8. Add command-line behaviour and exit codes.
9. Test edge cases, refactor, and document decisions.

Make a small commit after each completed milestone.

## Minimum test checklist

Write at least 25 meaningful tests. Include:

- valid and invalid IDs;
- missing CSV columns;
- duplicate records;
- unknown asset references;
- timestamp-ordering errors;
- exact SLA boundaries;
- unresponded orders measured using `--as-of`;
- repeat faults exactly on the window boundary;
- overlapping repeat-fault cases;
- malformed and mismatched notes;
- `Decimal` cost totals;
- score tie-breaking;
- strict and non-strict modes;
- all three exit codes;
- deterministic outputs from repeated runs.

## Definition of done

- All required inputs, rules, analyses, outputs, and exit codes work.
- `pytest` passes with at least 25 useful tests.
- A new user can run the project by following your README.
- The reports are deterministic and easy to inspect.
- Your code is split into functions and classes with clear responsibilities.
- No real employer data or secrets are committed.
- `REFLECTION.md` explains three bugs you found, two design decisions, and one feature you would build next.

## Optional extensions

Only attempt these after the required version is complete:

- Create a simple chart from `asset_report.csv`.
- Add date-range filters.
- Export a standalone HTML report.
- Add a second note format without breaking the first.
- Package the application with `pyproject.toml`.
