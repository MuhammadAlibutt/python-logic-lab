# Project 04 — Maintenance Note Regex Parser

**Timebox:** 75–105 minutes  
**Skills:** regex search/groups/boundaries, ambiguity handling, `datetime`, tests

## Objective

Extract structured fields from a human-written maintenance note without using an AI extraction service.

## Fields

### Work order — required

Accept exactly five digits in `WO-48291`, `WO 48291`, or `WO#48291`, case-insensitively. Normalise to `WO-48291`. Do not partially accept six digits.

### Equipment — required

Allowed prefixes: `CV`, `SC`, `PLC`, `BHS`. Accept a hyphen, underscore, or space followed by exactly two digits. Normalise `cv_12` to `CV-12`. Do not partially accept three digits.

### Date — required

Find `YYYY-MM-DD` with regex, then confirm it is a real calendar date using `datetime`.

### Owner email — optional

Accept a practical email containing letters/digits and common punctuation in the local part, one `@`, a dotted domain, and a final alphabetic suffix of at least two letters. Exclude trailing sentence punctuation and store lowercase. If absent, use `unassigned`.

## Required behaviour

- Each required field must occur exactly once.
- A missing required field names what is missing.
- More than one candidate in any category is ambiguous and invalid.
- Multiple missing fields are listed in fixed order: `work order, equipment, date`.
- An impossible calendar date is invalid even if its shape matches.
- Parsing returns structured data; the CLI catches and displays expected errors.

Example:

```text
Input: On 2026-09-01, WO#48291 reports cv_12 motor overheating; owner Ali.Khan@Example.COM.

Work order: WO-48291
Equipment: CV-12
Date: 2026-09-01
Owner: ali.khan@example.com
```

## Tests to write

- All work-order separators and case normalisation
- Six-digit work order rejected rather than partially matched
- All equipment separators and allowed prefixes
- Three-digit equipment rejected
- Valid date, impossible date, valid/invalid leap day
- Email lowercasing and trailing punctuation
- Missing optional email
- Each missing required field
- Multiple work orders, equipment tags, and emails
- One complete successful parsed result

## Stretch

- Parse one note per line from a file.
- Write valid records and rejected notes to separate CSV files.
- Redact owner emails from the original notes.

## Definition of done

- Similar longer tokens cannot produce partial matches.
- Missing and ambiguous data give clear errors.
- Date validation goes beyond regex.
- At least twelve tests pass.
- You can explain every capture group and boundary.

Suggested commits:

```text
docs: define accepted note formats
test: add work order and equipment cases
feat: extract and normalise required fields
feat: validate dates and optional owner
test: cover missing and ambiguous notes
docs: record project 04 reflection
```

