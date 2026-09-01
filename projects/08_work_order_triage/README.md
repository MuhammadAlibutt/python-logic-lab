# Project 08 — Maintenance Work-Order Triage Pipeline

**Timebox:** 4–6 hours  
**Skills:** regex, CSV pipeline, dates, rule precedence, deterministic sorting, multi-file design, tests

## Objective

Read raw synthetic work orders, validate them, assign a team and priority, calculate an SLA deadline, and write accepted, rejected, and summary files. This is intentionally rule-based rather than AI-driven.

Input headers:

```text
ticket_id,reported_at,asset_id,description
```

Run:

```text
python main.py work_orders.csv output_folder
```

Outputs:

```text
triaged.csv
rejected.csv
summary.txt
```

## Validation

- Ticket: `WO-YYYY-NNN`; normalise uppercase and require its year to match `reported_at`.
- Timestamp: real `YYYY-MM-DD HH:MM`.
- Asset: exactly three letters, a hyphen, and three digits; normalise uppercase.
- Description: trim/collapse whitespace; require 10–200 characters.
- Duplicate ticket: first fully valid occurrence wins; invalid occurrences do not reserve the ID.

## Team rules

| Asset prefix | Team |
|---|---|
| `CNV`, `MTR` | Mechanical |
| `SCN`, `PLC` | Controls |
| `NET` | IT |
| Other valid prefix | General |

## Priority rules

Match complete words or phrases, case-insensitively. `firewall` must not match `fire`.

- `P1`: fire, smoke, injury, emergency stop, safety risk
- `P2`: stopped, will not start, jam, jammed, offline, failed, failure
- `P3`: intermittent, slow, noise, warning
- `P4`: none above

When several groups match, choose the highest severity.

SLA:

- P1: +1 hour
- P2: +4 hours
- P3: +24 hours
- P4: +72 hours

## Outputs

`triaged.csv`:

```text
ticket_id,reported_at,asset_id,team,priority,due_at,description
```

Sort by priority P1→P4, earliest report time, then ticket ID.

`rejected.csv` preserves input order and uses ordered reason codes:

```text
invalid_ticket_id;invalid_reported_at;ticket_year_mismatch;invalid_asset_id;invalid_description;duplicate_ticket_id
```

Only use `ticket_year_mismatch` when ticket and timestamp are otherwise parseable.

`summary.txt` includes accepted/rejected totals, all priority totals including zero, team totals alphabetically, and the earliest SLA ticket or `N/A`.

## Tests to write

- Ticket/asset normalisation and malformed forms
- Real timestamps and year matching
- Every team mapping and General fallback
- One keyword from every priority group
- Case-insensitivity, precedence, and the `firewall` boundary
- All SLA calculations including midnight crossing
- Description boundaries and whitespace collapse
- Duplicate behaviour, including an invalid first occurrence
- Multiple ordered rejection reasons
- Accepted/rejected sorting
- End-to-end temporary CSV producing all outputs

## Stretch

- Move rules to JSON configuration.
- Add working-hours SLA logic or an `--as-of` overdue flag.
- Generate a Markdown dashboard.

## Definition of done

- Validation, classification, storage, and CLI are separated.
- Output is deterministic.
- Every rule has test coverage.
- Invalid rows never crash or silently disappear.
- You can safely change a keyword or SLA without relying on AI.

Suggested commits:

```text
docs: define work order rules
feat: validate and normalise input fields
feat: assign teams priorities and deadlines
feat: write accepted rejected and summary files
test: cover rules and full pipeline
docs: record project 08 reflection
```

