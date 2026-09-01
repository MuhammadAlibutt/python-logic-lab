# Project 05 — Contact Data Cleaner

**Timebox:** 2–3 hours  
**Skills:** regex, CSV, normalisation, duplicates, sorting, exceptions, pytest

## Objective

Read a messy contact CSV, validate and normalise each record, remove duplicates, and write accepted and rejected files.

Run:

```text
python cleaner.py raw_contacts.csv output_folder
```

Input headers:

```text
name,email,phone
```

## Rules

### Name

- Trim outer whitespace and collapse repeated internal whitespace.
- Preserve capitalisation.
- After cleaning, require 2–60 characters and at least one letter.

### Email

- Trim and lowercase.
- Require exactly one `@`, no whitespace, a dotted domain, and a final alphabetic suffix of at least two letters.
- Treat this as a practical business pattern, not the complete email standard.

### UK mobile

Accept forms such as:

```text
07123 456789
07123-456-789
+44 7123 456789
0044 7123 456789
```

Store as `+447123456789`. Reject landlines, extensions, and wrong digit counts.

### Duplicates

- Compare normalised emails and phones.
- The first valid record wins.
- A later record is rejected if either value duplicates an accepted contact.
- An invalid row does not reserve its email or phone.

## Outputs

`clean_contacts.csv`:

```text
name,email,phone
```

Sort by cleaned name case-insensitively, then email.

`rejected_contacts.csv`:

```text
name,email,phone,reason
```

Keep rejected rows in input order. Join multiple reason codes in this order:

```text
invalid_name;invalid_email;invalid_phone;duplicate_email;duplicate_phone
```

## Tests to write

- Every accepted phone form and several invalid numbers
- Valid/invalid emails and lowercase normalisation
- Repeated name whitespace
- Duplicate email and duplicate phone after normalisation
- Multiple reasons in the required order
- Case-insensitive sorting
- Quoted CSV name containing a comma
- One end-to-end read/clean/write test using a temporary directory

## Stretch

- Add summary counts by rejection reason.
- Support JSON output or a `--dry-run` mode.

## Definition of done

- Both output schemas are exact and deterministic.
- Every validation rule has a test.
- Invalid input never crashes processing.
- You can explain why normalisation happens before duplicate checking.

Suggested commits:

```text
docs: define contact cleaning rules
feat: validate and normalise contact fields
feat: split accepted and rejected contacts
test: cover duplicates and csv workflow
docs: record project 05 reflection
```

