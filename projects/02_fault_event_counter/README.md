# Project 02 — Conveyor Fault Event Counter

**Timebox:** 60–75 minutes  
**Skills:** loops, tuples, dictionaries, counting, multi-rule sorting, tests

## Objective

Accept repeated fault events and produce a ranked shift summary.

Valid zones:

```text
T1, T2, T3, WORKSHOP
```

Valid faults:

```text
JAM, SENSOR, MOTOR, NETWORK, OTHER
```

## Required behaviour

- Repeatedly accept `ZONE,FAULT` until the user enters `done`.
- Ignore case and outer whitespace.
- Require exactly one comma and two non-empty valid values.
- Reject bad entries without altering counts.
- Count repeated events separately.
- Display total faults, totals by fault, totals by zone, and all busiest zones.
- Sort totals by descending count, with alphabetical ties.
- If no valid events exist, print `No valid fault events entered.`

Example result:

```text
Total valid faults: 5
By fault:
JAM: 3
MOTOR: 1
SENSOR: 1
By zone:
T1: 3
T2: 2
Busiest zone(s): T1
```

## Edge cases and tests

Test at least:

- `DONE`, ` Done `, and `done`
- Missing comma, extra comma, and empty fields
- Unknown zone and fault
- Case/whitespace normalisation
- Duplicate counting
- Descending count order
- Alphabetical tie order
- One busiest zone and several tied zones
- Empty input collection

## Stretch

- Count each fault within each zone using a nested dictionary.
- Show percentages and the most frequent fault for each zone.
- Save the report to a text file.

## Definition of done

- Parsing, aggregation, sorting, and terminal interaction are separate.
- Invalid events never change a count.
- Ties are deterministic.
- At least ten tests pass.
- You can rebuild the counting algorithm from pseudocode.

Suggested commits:

```text
docs: plan event format and report
test: add event parser cases
feat: parse and count fault events
feat: add ranking and tie handling
docs: record project 02 reflection
```

