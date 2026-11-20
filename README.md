# Library Late Fee Calculator — Assignment 3

A small Python application that calculates late fees for books, DVDs and magazines, with an optional student discount. Used for baseline/static-analysis and quality-improvement demonstrations.

## Requirements
Python 3.12, pytest, pytest-cov, GitHub Actions, SonarQube Cloud.

## Run tests locally
```bash
python -m pip install -r requirements.txt
python -m pytest -q --cov=fee_calculator --cov-report=xml:coverage.xml --cov-report=term-missing
```

## Assignment sequence
1. Push this baseline (after configuring SonarQube project identifiers and SONAR_TOKEN).
2. Record baseline commit SHA and confirm a successful workflow and Cloud scan.
3. Investigate at least 3 findings; SonarQube rules and severities depend on the actual scan.
4. Independently test negative days and unknown item types before applying the fixes.
5. Apply the final changes and tests from the separate final-changes ZIP.
6. Push the fix as a new commit, capture the final workflow and dashboard, compare metrics.

Never commit tokens or .env files.
