# Project 07 — Personal Expense Tracker CLI

**Timebox:** 3–4 hours  
**Skills:** multiple modules, CSV persistence, `Decimal`, dates, filtering, sorting, aggregation, tests

## Objective

Build a persistent command-line tracker that adds expenses, lists them, and produces monthly summaries.

Data schema:

```text
id,date,category,amount,note
```

IDs use `EXP-0001`, increasing from the highest stored number without reusing gaps.

Allowed categories:

```text
food, transport, bills, learning, social, other
```

## Commands

```text
python main.py add 2026-09-01 food 12.50 "Dinner with friends"
python main.py list
python main.py list 2026-09
python main.py summary
python main.py summary 2026-09
```

## Validation

- Real dates use `YYYY-MM-DD`; month filters use valid `YYYY-MM`.
- Money accepts `5`, `5.5`, or `5.50` and is stored/displayed to two decimals.
- Reject zero, negative, scientific notation, more than two decimals, and amounts over `999999.99`.
- Use `Decimal`, not binary floating point.
- Categories are case-insensitive and stored lowercase.
- Notes are trimmed, internal whitespace collapsed, and 1–80 characters.
- Invalid commands show usage without a traceback.

## Persistence and reports

- Create the data folder/file on first successful add.
- `list` or `summary` before a file exists behaves as an empty tracker.
- Validate existing headers and rows; corrupted stored data must name the row and must not be silently changed.
- List newest dates first; for equal dates, highest ID first.
- Summary shows transaction count, total, totals by category, and largest expense.
- Sort category totals descending, with alphabetical ties.

## Tests to write

- Valid and invalid money forms
- Real/invalid dates and month filters
- Category and note normalisation
- Next ID with gaps
- First-file creation and correct header
- Round-trip a note containing a comma
- Same-date sorting and monthly filtering
- Exact total calculations
- Category tie ordering and largest expense
- Invalid header, invalid stored row, and duplicate stored ID

## Stretch

- Add deletion, monthly budgets, or Markdown export.

## Definition of done

- Commands still work after closing and reopening the program.
- Money is exact.
- Storage, business logic, and CLI are separated.
- Tests use temporary paths rather than your real data file.
- You can explain why `Decimal` is appropriate.

Suggested commits:

```text
docs: define expense commands and schema
feat: validate expenses and generate ids
feat: persist expenses in csv
feat: add list filters and summaries
test: cover storage calculations and errors
docs: record project 07 reflection
```

