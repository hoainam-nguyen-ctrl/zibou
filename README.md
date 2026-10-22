# zibou

Minimal Python project.

## Requirements

- Python 3.11+

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Usage

```python
from zibou import hello

print(hello("Zibou"))
```

## Development

```bash
pytest          # run tests
ruff check .    # lint
ruff format .   # format
```

## Structure

```
zibou/
├── pyproject.toml
├── src/zibou/__init__.py
└── tests/test_zibou.py
```
