# Practice Rules

## The workflow for every project

1. Create `PLAN.md` in the project folder.
2. Restate the problem, inputs, outputs, rules, and constraints in your own words.
3. Work through at least two examples by hand.
4. Write pseudocode before Python.
5. Spend at least 45 minutes independently before asking AI for help.
6. Ask for a concept explanation or one hint before asking for code.
7. Write tests for small functions before or alongside the implementation.
8. Test normal, empty, invalid, and boundary cases.
9. Refactor only after the behaviour works.
10. Update the project README with what you learned and what remains imperfect.
11. Rebuild the core function from a blank file within 72 hours.

## AI help ladder

Use AI in this order:

1. “Explain the concept with a different small example.”
2. “Give me one hint, not code.”
3. “Review my pseudocode and identify the first incorrect assumption.”
4. “Review my failing test and ask diagnostic questions.”
5. “Review my code; do not rewrite it.”

If you finally need generated code, record why in `REFLECTION.md`, explain every line, close the answer, and rebuild the important part yourself.

## Suggested commit sequence

Use small commits that reveal your thinking:

```text
docs: add plan and examples for project 01
test: add validator edge cases
feat: implement asset id validation
refactor: simplify validation flow
docs: record project 01 reflection
```

Do not make one commit containing the entire completed project.

## Definition of honest completion

A project counts only when:

- All required behaviours work.
- Tests cover the core logic and edge cases.
- You can explain every line without AI.
- The README includes usage examples.
- `REFLECTION.md` states one mistake, one lesson, and one next improvement.
- The core logic was rebuilt from memory within 72 hours.

