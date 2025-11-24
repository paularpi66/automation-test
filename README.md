# QA Automation — Python Selenium (POM)

This is a small Python Selenium test automation project using Page Object Model (POM).
It tests a sample website https://practicesoftwaretesting.com/ for:

1. Contact form validation and submission
2. Add-to-cart functionality and quantity update


## Prerequisites

- Python 3.8+ installed

- Google Chrome installed (or Firefox if configured)

- `pip` for installing dependencies

## Setup

1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests

```bash
pytest -q
```

Run a single test file

```bash
pytest tests/test_contact_form.py -q
```

Run with browser visible (not headless)

```bash
HEADLESS=false pytest -q
```
