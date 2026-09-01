# Project 06 — Multi-File Log Investigator

**Timebox:** 3–4 hours  
**Skills:** regex groups, directory/file processing, `datetime`, counters, sorting, reports, tests

## Objective

Read all `.log` files in one directory, parse structured entries, count failures, track malformed lines, and write a deterministic report.

Valid line format:

```text
YYYY-MM-DD HH:MM:SS | LEVEL | component_name | message
```

Rules:

- Timestamp must be a real date and time.
- Level is `INFO`, `WARNING`, `ERROR`, or `CRITICAL`.
- Component starts lowercase and contains lowercase letters, digits, or underscores.
- Message is non-empty and may itself contain `|`; everything after the third separator belongs to the message.
- Blank lines are ignored.

Run:

```text
python main.py sample_logs report.txt
```

## Required report

Include:

- Files scanned
- Valid and malformed entry counts
- Earliest and latest valid timestamps, or `N/A`
- Count of every level
- Failures (`ERROR` + `CRITICAL`) by component
- Top failure component; highest count wins and alphabetical order breaks ties
- Each malformed location as `filename:line_number`

Process filenames alphabetically. Sort failure components by descending count, then alphabetically.

Example valid entries:

```text
2026-09-01 08:32:10 | INFO | conveyor_api | Service started
2026-09-01 09:02:11 | ERROR | baggage_db | Database unavailable | retry scheduled
```

## Error behaviour

- Missing/non-directory path or no `.log` files → friendly error, no report.
- Empty log files still count as scanned.
- Files with no valid entries produce a report with `N/A` timestamps.
- A read failure must be reported, not ignored.

## Tests to write

- Parse a valid line into fields
- Preserve pipes inside the message
- Reject each invalid field and impossible dates
- Ignore blank lines
- Count levels and failures correctly
- Resolve top-component ties alphabetically
- Calculate earliest/latest independent of file order
- Report one-based malformed line locations
- Scan temporary `.log` files while ignoring unrelated files

## Stretch

- Export malformed lines to CSV.
- Filter by minimum severity or component.
- Detect repeated identical error messages.

## Definition of done

- Parser and report logic are testable without the CLI.
- File order cannot alter output.
- Malformed input never crashes the run.
- Tests cover parsing, aggregation, sorting, and directory workflow.

Suggested commits:

```text
docs: define log format and report
feat: parse and validate log entries
feat: aggregate multiple log files
feat: generate deterministic report
test: cover parser and directory workflow
docs: record project 06 reflection
```

