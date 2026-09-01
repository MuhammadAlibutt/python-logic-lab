# Project 03 — Airport Asset ID Validator

**Timebox:** 60–90 minutes  
**Skills:** regex, normalisation, functions, business-rule validation, pytest

## Objective

Validate and explain synthetic airport asset identifiers. This is your first focused regex project.

## Accepted format

```text
AAA-AA-0000
```

Rules:

- First group: exactly three letters identifying a system.
- Second group: exactly two letters identifying an equipment type.
- Final group: exactly four digits.
- Hyphens are required; internal spaces are invalid.
- Lowercase input and outer whitespace may be normalised.
- Serial `0000` is invalid even though it has the correct shape.
- The entire string must match; valid text inside a longer string is not enough.

Examples:

```text
bhs-me-0421       -> valid as BHS-ME-0421
 SEC-SC-0007      -> valid as SEC-SC-0007
BHS ME 0421       -> invalid separator
BHS-MECH-0421     -> invalid equipment group
BHS-ME-0000       -> invalid reserved serial
XXBHS-ME-0421YY   -> invalid extra text
```

## Required behaviour

Create separate logic for:

- Normalising a candidate
- Checking its structural format with regex
- Applying non-regex business rules
- Returning a useful failure reason
- Terminal interaction

Required failure categories:

```text
empty
invalid_format
reserved_serial
```

The program should accept one ID or optionally continue until `done`.

## Tests to write

- Valid uppercase and lowercase values
- Outer whitespace
- Empty and whitespace-only input
- Wrong group lengths
- Missing, extra, and wrong separators
- Letters where digits belong and digits where letters belong
- Reserved serial `0000`
- Prefix/suffix text that must not partially match
- Newline at the end of input

## Stretch

- Read one candidate per line from a file and report valid/invalid totals.
- Count valid assets by system code.

## Definition of done

- Regex checks shape; ordinary Python checks the reserved serial.
- No partial match is accepted.
- Failure reasons are testable without printing.
- At least ten tests pass.
- You can draw and explain every part of the pattern on paper.

Suggested commits:

```text
docs: define asset id rules and examples
test: add valid and invalid asset identifiers
feat: validate and normalise asset ids
feat: add clear validation reasons
docs: record project 03 reflection
```

