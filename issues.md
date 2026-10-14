# Lab 5: Static Code Analysis — Issues Found

Line numbers below refer to the original `dairy_collection.py` before fixes.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 hash | Security — High | 16 | Bandit B324 flagged MD5 as a weak hash algorithm. | Replaced MD5 with SHA-256 for the deterministic demonstration identifier. This identifier is not suitable for authentication. |
| Shell command execution | Security — High | 31 | Bandit B605 flagged `os.system()` with concatenated input, which can permit command injection. | Replaced shell execution with Python's `print()` function. |
| SQL query built by string formatting | Security — Medium | 11 | Bandit B608 flagged a query constructed by interpolating values into SQL. | Changed the insert to a parameterized query using `?` placeholders and a tuple of values. |
| Missing module docstring | Code quality | 1 | Pylint C0114 reported that the module had no docstring. | Added a module-level docstring. |
| Missing function docstrings | Code quality | 10, 15, 19, 24, 30, 34, 39 | Pylint C0116 reported missing function docstrings. | Added concise docstrings to each function. |
| CamelCase function names | Code quality | 10, 15, 19, 24, 30, 34 | Pylint C0103 reported names that did not follow snake_case. | Renamed functions to snake_case and updated their call sites. |
| Redefined outer `conn` name | Code quality | 10, 19, 24, 34 | Pylint W0621 reported parameters shadowing the module-level connection. | Removed the global connection and create/manage the connection in `main()`, passing it to the relevant functions. |
| Unused import | Style | 2 | Pylint W0611 and Flake8 F401 reported that `json` was unused. | Removed the import. |
| Lines too long | Style | 7, 11, 20, 25 | Pylint C0301 and Flake8 E501 reported long lines. | Split SQL and other statements across multiple lines. |
| Old-style string formatting | Style | 11, 21 | Pylint C0209 flagged `.format()` and `%` formatting where f-strings could be used. | Used parameterized SQL for the insert and an f-string for the total display. |
| Ambiguous variable name | Style | 26 | Flake8 E741 flagged the variable `l`. | Replaced it with descriptive names and a direct `fetchone()` query. |
| Comparison to None | Style | 36 | Pylint C0121 and Flake8 E711 flagged `fat == None`. | Changed the comparison to `fat is None`. |
| Empty ledger edge case | Robustness | 26 | `max()` would raise `ValueError` if there were no delivery records. | `top_farmer()` now returns `None` when the ledger is empty. |

## Verification
After applying the fixes, I reran the program and the static analysis tools.

- **Pylint:** 10.00/10, with no issues identified.
- **Bandit:** No issues identified; zero findings across all severity levels.
- **Flake8:** No violations reported.
- **Program execution:** The program ran successfully and retained its expected dairy collection functionality.

The final analysis showed a significant improvement in code quality, with no findings from the completed Pylint and Bandit scans.