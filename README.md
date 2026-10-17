# AttendX-Test-Scripts

Automation test scripts for AttendX, the student attendance application.
All scripts are kept under Git so the three QA engineers stop overwriting each other's work.

## Scripts

| File | What it tests |
|---|---|
| `login_test.py` | A valid user can log in and reach the dashboard |
| `attendance_test.py` | A teacher can mark a student present and see a success message |

## Requirements

- Python 3.9+
- Selenium: `pip install selenium`
- Google Chrome

## How to run

```
python login_test.py
python attendance_test.py
```

Change `BASE_URL` at the top of each script to point to the AttendX site.

## Team workflow

1. `git pull` before you start work
2. Make your change
3. `git add`, `git commit -m "clear message"`
4. `git push`

## test line
