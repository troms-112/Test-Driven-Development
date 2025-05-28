# A2: TDD Hands-On (CS 362 Assignment 2)

This repository contains an exercise in Test-Driven Development (TDD) for implementing a password-validation function, **`check_pwd`**, according to the following specification:

> **`check_pwd(pwd: str) → bool`**  
> Returns `True` if and only if the input string meets **all** of the following criteria:
> 1. Length between **8** and **20** characters (inclusive).  
> 2. Contains **at least one** lowercase letter (`a–z`).  
> 3. Contains **at least one** uppercase letter (`A–Z`).  
> 4. Contains **at least one** digit (`0–9`).  
> 5. Contains **at least one** symbol from  
>    ```
>    ~ ` ! @ # $ % ^ & * ( ) _ + - =
>    ```

## Getting Started

1. **Clone** your private GitHub repo and ensure you have Python 3.7+ installed:
   ```bash
   git clone git@github.com:<your-org>/Test-Driven-Development.git
   cd test-driven-development
   ```

2. **Run the tests**:
   ```bash
   python3 -m unittest test_check_pwd.py
   ```

   You should see failures at first, then green as you implement each feature.

## TDD Workflow

Follow these steps for each new behavior:

1. **Write a single test** in `test_check_pwd.py` that **fails**.  
2. **Commit** with message:
   ```
   Wrote testX: <brief description of what it tests>
   ```
3. **Implement** the smallest amount of code in `check_pwd.py` to make that test pass.  
4. **Commit** with message:
   ```
   Made check_pwd handle <what you just implemented>
   ```
5. **Repeat** until all specification points are covered and tests pass.

> **Important:**  
> - **Do not** write more than one test at a time.  
> - **Commit twice** per cycle: once after adding the test (failing), once after implementing the code (passing).  
> - **Never** modify an existing test once committed.  
> - Keep implementation and tests lint-clean under PEP8.

## Running & Extending

- To re-run the full suite:
  ```bash
  python3 -m unittest discover
  ```
- To experiment or add edge-case tests, create new methods in `test_check_pwd.py` following the naming convention `testN_…`.
- Always follow the TDD cycle above when adding tests or code.

## Commit Guidelines

- **Test commits** (failing):  
  ```
  Wrote testX: <what you’re testing>
  ```
- **Implementation commits** (passing):  
  ```
  Made check_pwd <description of new capability>
  ```
- Keep each commit focused—one test or one minimal code change.

---

*This project meets CLO4 (automated testing) and demonstrates disciplined application of TDD practices.*  
