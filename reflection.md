# Lab 5: Static Code Analysis — Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were the unused import, incorrect comparison with `None`, long lines, and function naming conventions. These required straightforward changes without significantly affecting the program's logic.

The hardest issues were the potential SQL injection vulnerability, the use of `os.system()`, and the weak MD5 hash. These required understanding the security implications and choosing safer alternatives while preserving the program's functionality.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

The tools reported potential issues rather than confirmed vulnerabilities. For example, Bandit flagged the use of MD5 because it is considered a weak cryptographic hash. In this program, the hash was only used to generate a deterministic identifier for a farmer's name, not for password storage or authentication. Therefore, the finding highlighted a potentially unsafe practice, although the actual risk depended on how the hash was used.

Bandit's SQL injection warning identified a genuine risk in constructing SQL queries using string formatting, so that finding was not a false positive.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would run Pylint, Bandit, and Flake8 regularly during development, especially before committing or pushing code. I would also integrate them into a GitHub Actions workflow so that code is checked automatically whenever a pull request is created. High-severity security findings would be prioritized, while style and maintainability issues would be addressed alongside feature development.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The code became more readable through consistent snake_case function names, descriptive variables, docstrings, and improved formatting. Parameterized SQL queries reduced the risk of SQL injection, and replacing `os.system()` with `print()` removed unnecessary shell execution. Replacing MD5 with SHA-256 improved the hash algorithm choice for the deterministic identifier. The code also handled an empty ledger more safely by returning `None` when no top farmer exists.

After the changes, Pylint's score increased from 2.00/10 to 10.00/10, and Bandit reported no remaining findings. These results indicate a substantial improvement in the code's compliance with the tools' checks.