# demo-fake-py3.9

A small, intentionally fictitious Python 3.9 codebase used as a test fixture for Genie's
"Language or runtime upgrade" modernization capability.

## Layout

- `calc.py` - math/arithmetic/geometry/statistics utility functions
- `db_ops.py` - SQLite database operation helpers (connections, CRUD, transactions, import/export)
- `str_ops.py` - string manipulation utility functions
- `tests/` - pytest unit tests covering all three modules
- `Dockerfile` - `python:3.9-slim` base image, used by Genie's dependency assessment to detect
  the current runtime version
- `requirements.txt` - pytest only (no other third-party dependencies)

This repository intentionally targets Python 3.9 so that a "Language or runtime upgrade" plan
has real, evidenced work to do (e.g. upgrading to a newer Python version and adjusting the
`typing.List`/`typing.Union`-style type hints used throughout to the modern built-in generic
and `X | Y` union syntax, if targeting Python 3.10+).
