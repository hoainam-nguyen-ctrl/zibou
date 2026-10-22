# zibou

Minimal Flask application, served with gunicorn and shipped as a Docker image.

## Endpoints

| Method | Path      | Response                                  |
|--------|-----------|-------------------------------------------|
| GET    | `/`       | `{"message": "Hello from zibou!"}`        |
| GET    | `/health` | `{"status": "ok", "version": "0.1.0"}`    |

## Local development

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

flask --app "zibou:create_app()" run --debug   # dev server on http://127.0.0.1:5000
pytest                                          # tests
ruff check . && ruff format .                   # lint / format
```

Configuration: any environment variable prefixed `ZIBOU_` is loaded into the Flask config
(e.g. `ZIBOU_SECRET_KEY`). Never commit secrets; pass them at runtime.

## Docker

```bash
docker build -t zibou .
docker run --rm -p 8000:8000 zibou
curl http://localhost:8000/health
```

The image is multi-stage, runs as a non-root user (uid 10001), exposes port 8000 and has a
built-in healthcheck on `/health`.

## CI

`.github/workflows/ci.yml` runs on every push and pull request:

1. **test**: ruff lint + format check, pytest
2. **image**: builds the Docker image; on `main` it is pushed to
   `ghcr.io/hoainam-nguyen-ctrl/zibou` with tags `latest` and `sha-<commit>`.
   The package inherits the repository's private visibility.

## Structure

```
zibou/
├── .github/workflows/ci.yml
├── Dockerfile
├── .dockerignore
├── pyproject.toml
├── src/zibou/__init__.py   # create_app() factory
└── tests/test_zibou.py
```
