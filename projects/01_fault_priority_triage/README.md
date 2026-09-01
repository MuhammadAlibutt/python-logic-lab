# Project 01 — Equipment Fault Priority Triage

**Timebox:** 45–60 minutes  
**Skills:** functions, conditionals, input validation, exceptions, pytest

## Objective

Turn written maintenance rules into reliable conditional logic. Build a terminal program that collects a fault report and assigns priority `P1`–`P4`.

## Required input

Ask for:

1. Equipment ID
2. Whether there is a safety risk
3. Whether the equipment is completely stopped
4. Downtime/disruption minutes

Rules:

- Trim and uppercase the equipment ID; reject an empty value.
- Accept `yes`, `y`, `no`, and `n`, ignoring case and outer whitespace.
- Minutes must be a whole number of zero or more.
- Invalid terminal input must be requested again without a traceback.

## Priority rules

Evaluate in this order:

1. Safety risk → `P1`
2. No safety risk, stopped for at least 30 minutes → `P1`
3. Stopped for fewer than 30 minutes → `P2`
4. Not stopped, disruption at least 60 minutes → `P2`
5. Not stopped, disruption from 1 to 59 minutes → `P3`
6. Not stopped, zero disruption → `P4`

Messages:

- `P1: Escalate immediately`
- `P2: Attend this shift`
- `P3: Schedule inspection`
- `P4: Monitor`

Example:

```text
Equipment ID: cv-104
Safety risk (yes/no): no
Equipment stopped (yes/no): yes
Downtime minutes: 45
CV-104 | P1 | Escalate immediately
```

## Design requirements

Separate terminal interaction from logic. Useful function responsibilities include normalising yes/no input, classifying priority, and formatting a report. You choose the names and implementation.

## Tests to write

At minimum, test:

- All accepted yes/no variations and one invalid value
- Safety risk always gives P1
- Stopped at 29 and 30 minutes
- Not stopped at 59 and 60 minutes
- Zero minutes with no stop
- Negative, decimal, and non-numeric minutes
- Equipment ID normalisation

## Stretch

- Process several faults and print counts per priority.
- Add a timestamp using `datetime`.

## Definition of done

- Every priority is reachable.
- Boundaries `0`, `29`, `30`, `59`, and `60` are correct.
- Logic functions can be tested without `input()`.
- At least eight meaningful tests pass.
- You can explain why the conditions must be evaluated in this order.

Suggested commits:

```text
docs: plan fault priority rules
test: add priority boundary cases
feat: implement fault priority triage
refactor: separate input from classification
docs: record project 01 reflection
```

