# demo-fake-py3.9

This is a small demo repository showcasing simple Python utility modules (`calc.py`, `db_ops.py`, `str_ops.py`) and their associated unit tests using `pytest`.

Originally the project targeted Python 3.9. It has now been verified to run on **Python 3.12**.

## Requirements

- Python 3.12
- `pip`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Running tests

```bash
pytest
```

## Container usage

A minimal `Dockerfile` is provided which uses the official `python:3.12-slim` image, installs dependencies from `requirements.txt`, and runs the pytest suite by default.

To build and run tests in a container:

```bash
docker build -t demo-fake-py312 .
docker run --rm demo-fake-py312
```
