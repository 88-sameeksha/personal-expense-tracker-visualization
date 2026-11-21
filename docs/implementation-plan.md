# Implementation Plan

| Phase | Task | Expected result |
|---|---|---|
| 1 | Install Python and create venv | Isolated environment |
| 2 | Create project folders and modules | Organized codebase |
| 3 | Create or inspect expenses.csv | Structured input |
| 4 | Load CSV with Pandas | DataFrame |
| 5 | Clean dates, amounts and labels | Valid transactions |
| 6 | Group by category | Category summary |
| 7 | Group by month and day | Spending trends |
| 8 | Generate four charts | PNG visualizations |
| 9 | Export CSV and text reports | Shareable outputs |
| 10 | Commit and push to GitHub | Public proof of work |

## Beginner mistakes to avoid

- Running commands from the wrong directory.
- Forgetting to activate the virtual environment.
- Misspelling CSV column names.
- Entering currency symbols in the numeric amount column.
- Using inconsistent date formats.
- Committing `.venv/` or secret information.
- Forgetting to close Matplotlib figures (the project closes each figure).
