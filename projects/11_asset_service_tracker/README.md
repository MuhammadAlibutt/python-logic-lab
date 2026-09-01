# Project 11 — Asset Service Tracker

**Start only after the CS50P OOP week.**  
**Timebox:** 6–8 hours  
**Skills:** classes, properties, composition, JSON persistence, custom exceptions, CLI tests

## Objective

Register synthetic airport assets, record service history, and report assets that are overdue or approaching their next service.

## Required object model

### `ServiceRecord`

Owns service date, technician, and notes. It validates its own state, has a useful string representation, and converts to/from JSON-compatible data.

### `Asset`

Owns asset ID, name, location, commissioned date, service interval in days, and `ServiceRecord` objects. It can add a service, find the latest service, calculate next service, determine status for a supplied date, and serialize/deserialize.

Next service is latest service + interval, or commissioned date + interval when there is no history.

### `AssetTracker`

Owns the asset collection. It registers/finds assets, records service, queries due assets, and loads/saves state.

Use composition—an asset contains service records. Do not add inheritance merely to demonstrate syntax.

Use meaningful exceptions for validation, duplicate asset, and asset not found. Catch them in the CLI.

## Suggested commands

```text
python tracker.py --data tracker.json add-asset BHS-1001 --name "Transfer Belt 1" --location "T1 Merge" --commissioned 2026-01-15 --interval 30
python tracker.py --data tracker.json record-service BHS-1001 --date 2026-08-15 --technician "A Khan" --notes "Inspected belt tension"
python tracker.py --data tracker.json show BHS-1001
python tracker.py --data tracker.json due --as-of 2026-09-20 --within 14
python tracker.py --data tracker.json list
```

Statuses:

- `OVERDUE`: next date before `as-of`
- `DUE TODAY`: equal to `as-of`
- `DUE SOON`: after `as-of`, within the window
- `OK`: beyond the window

Sort by next-service date, then asset ID.

## Edge cases/tests

Test:

- Invalid state in every class
- Duplicate and unknown assets
- Invalid/impossible dates and non-positive interval
- Service before commissioning
- Services inserted out of date order; latest must still win
- No-service calculation
- All four status boundaries
- Save/load round trip, empty file, malformed JSON, missing fields
- Deterministic due sorting
- CLI non-zero result for invalid data

## Stretch

- Update location/interval, export due list to CSV, or add atomic saves.

## Definition of done

- Classes own their behaviour; outside code does not manipulate their internals carelessly.
- CLI, domain objects, and storage are separated.
- State survives program restarts.
- At least eighteen tests pass.
- README explains why every class exists and why composition was chosen.

Suggested commits:

```text
docs: design asset service object model
feat: add service record validation
feat: add asset service calculations
feat: add tracker and domain exceptions
feat: persist state and add cli
test: cover models persistence and boundaries
docs: record project 11 reflection
```

