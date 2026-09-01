# Python Logic Lab

A solution-free sequence of Python projects for practising the material in Harvard's CS50P course. The projects grow from focused regular-expression exercises into a multi-feature intermediate command-line application.

This repository is a learning record. Every finished project should show the problem-solving process, tests, meaningful Git history, and a short reflection—not only the final code.

## Start here

1. Use [`TODAY.md`](TODAY.md) for your first focused session.
2. Read [`PRACTICE_RULES.md`](PRACTICE_RULES.md).
3. Begin with [`projects/01_fault_priority_triage`](projects/01_fault_priority_triage/README.md).
4. Complete projects in order unless a specification says that it requires a later CS50P topic.
5. Update [`PROGRESS.md`](PROGRESS.md) every Sunday.
6. Never commit company data, internal manuals, customer information, credentials, or copied production code. All supplied examples are synthetic.

## Project path

| # | Project | Main CS50P skills | Time guide | Status |
|---:|---|---|---:|---|
| 01 | [Equipment Fault Priority Triage](projects/01_fault_priority_triage/README.md) | Functions, conditionals, exceptions, tests | 45–60 min | ☐ |
| 02 | [Conveyor Fault Event Counter](projects/02_fault_event_counter/README.md) | Loops, dictionaries, sorting, ties | 60–75 min | ☐ |
| 03 | [Airport Asset ID Validator](projects/03_asset_id_validator/README.md) | Functions, regex, validation, tests | 60–90 min | ☐ |
| 04 | [Maintenance Note Regex Parser](projects/04_maintenance_note_parser/README.md) | Regex groups, dates, ambiguity, tests | 75–105 min | ☐ |
| 05 | [Contact Data Cleaner](projects/05_contact_data_cleaner/README.md) | Regex, CSV, normalisation, duplicates | 2–3 hours | ☐ |
| 06 | [Multi-File Log Investigator](projects/06_log_investigator/README.md) | Regex, files, aggregation, deterministic reports | 3–4 hours | ☐ |
| 07 | [Personal Expense Tracker](projects/07_expense_tracker/README.md) | Decimal, CSV persistence, filtering, tests | 3–4 hours | ☐ |
| 08 | [Work-Order Triage Pipeline](projects/08_work_order_triage/README.md) | Business rules, regex, CSV, dates, tests | 4–6 hours | ☐ |
| 09 | [Maintenance CSV Roll-Up](projects/09_maintenance_csv_rollup/README.md) | File errors, row errors, aggregation, tests | 2–3 hours | ☐ |
| 10 | [Persistent Task Tracker](projects/10_persistent_task_tracker/README.md) | JSON, exceptions, CLI design, tests | 4–5 hours | ☐ |
| 11 | [Asset Service Tracker](projects/11_asset_service_tracker/README.md) | Classes, composition, JSON, tests | 6–8 hours | ☐ |
| 12 | [Maintenance Operations Analyzer](projects/12_maintenance_operations_analyzer/README.md) | Full course integration | 10–15 hours | ☐ |

Projects 01–10 use topics already covered by or around the regular-expression stage. Projects 01 and 02 deliberately revisit fundamentals because logic grows through repetition, not by using advanced syntax. Project 11 should wait until the CS50P OOP week. Project 12 is the capstone and should begin only after Project 11.

## Recommended eight-week rhythm

| Week | Course and project target |
|---:|---|
| 1 | Resume regex; complete Projects 01–03 |
| 2 | Complete Project 04 and begin Project 05 |
| 3 | Finish Project 05 and complete Project 09 |
| 4 | Complete Project 06 |
| 5 | Complete Project 07 |
| 6 | Complete Projects 08 and 10, using extra days if needed |
| 7 | Finish OOP; complete Project 11; design the capstone |
| 8 | Build Project 12; use a second week for tests, documentation, and polish |

The timetable is a guide. A project is complete only when its definition of done is met.

## Running tests

Create a virtual environment, install the development requirement, and run tests from the individual project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest
```

Do not run all repository tests until you have written them. Initially, unfinished project folders intentionally contain specifications rather than solutions.
