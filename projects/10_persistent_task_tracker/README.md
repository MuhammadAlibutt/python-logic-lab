# Project 10 — Persistent Command-Line Task Tracker

**Timebox:** 4–5 hours  
**Skills:** JSON persistence, CRUD-like logic, IDs, dates, filters, sorting, exceptions, pytest

## Objective

Build a task tracker whose data survives separate program runs. Support add, list, show, update, status changes, and delete.

Each task stores:

```text
id, title, category, priority, status, created_on, due_on, completed_on
```

Rules:

- ID: automatically generated `TASK-0001`; deleted IDs are never reused.
- Title: 3–80 trimmed characters.
- Category: `STUDY`, `PROJECT`, `CAREER`, `PERSONAL`.
- Priority: `LOW`, `MEDIUM`, `HIGH`.
- Status: `TODO`, `DOING`, `DONE`.
- Dates: real `YYYY-MM-DD`; due/completion cannot predate creation.
- Only a `DONE` task has `completed_on`; reopening clears it.

## Storage

Use:

```json
{
  "next_id": 2,
  "tasks": []
}
```

- Missing file means a new empty tracker.
- Blank, malformed, or structurally invalid existing JSON is an error; never silently replace it.
- Save with stable indentation/key ordering, numeric ID order, and a final newline.
- A failed mutation must leave the original file unchanged.
- `next_id` remains higher than every allocated ID, even after deletion.

## Commands

```text
python task_tracker.py --data tasks.json add "Finish regex exercises" --category STUDY --priority HIGH --created 2026-09-01 --due 2026-09-05
python task_tracker.py --data tasks.json list
python task_tracker.py --data tasks.json show TASK-0001
python task_tracker.py --data tasks.json update TASK-0001 --priority MEDIUM --due 2026-09-07
python task_tracker.py --data tasks.json set-status TASK-0001 DONE --on 2026-09-04
python task_tracker.py --data tasks.json set-status TASK-0001 TODO
python task_tracker.py --data tasks.json delete TASK-0001
```

Update requires at least one change. Support `--clear-due`; it is mutually exclusive with `--due`.

## Filters and sorting

List filters:

```text
--status TODO
--priority HIGH
--category STUDY
--overdue --as-of 2026-09-10
--due-by 2026-09-15
```

Multiple filters use AND. An overdue task is not done and has a due date before—not equal to—`as-of`.

Sort by `id`, `due`, `priority`, `created`, or `title`:

- Default: numeric ID.
- Due: earliest first, missing last.
- Priority: HIGH, MEDIUM, LOW.
- Title: case-insensitive.
- Every tie breaks by numeric ID.
- Filter before sorting.

## Load validation

Reject stored data with missing keys/fields, malformed or duplicate IDs, invalid `next_id`, unknown enums, invalid dates, or impossible due/completion/status combinations.

## Tests to write

Aim for at least 20 tests covering:

- First/sequential IDs and no reuse after deletion
- Field and date boundaries
- Missing file versus malformed JSON
- Duplicate IDs and invalid `next_id`
- Deterministic save/load round trip
- Unknown task handling
- Single/multiple updates and no-change update
- Clearing due date
- Completing/reopening a task
- Delete success/failure
- Every filter, combined filters, and overdue boundary
- Every sort mode, missing dates, and tie-breaking
- Failed mutation leaves storage unchanged
- CLI success/failure exit codes

## Stretch

- Add tags, search, summary, archive, CSV export, or atomic temporary-file saves.

## Definition of done

- All commands work across separate runs.
- IDs are never reused.
- Filters combine and output is deterministic.
- Invalid commands never partially modify storage.
- You can explain the responsibilities of CLI, business logic, and persistence code.

Suggested commits:

```text
docs: define task tracker commands and rules
feat: load validate and save tracker state
feat: add task creation and id generation
feat: add show update status and delete
feat: add filters and deterministic sorting
test: cover persistence mutations and queries
docs: record project 10 reflection
```

