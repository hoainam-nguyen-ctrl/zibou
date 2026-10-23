# zibou

Flask + htmx app, served by gunicorn in Docker. Deployment and infrastructure are described in
`~/CLAUDE.md` on the server, not in this repo.

## Layout

- `src/zibou/__init__.py`: `create_app()` factory and all routes (`/`, `/hello`, `/health`).
- `src/zibou/templates/`: `index.html` is the page; files prefixed `_` are htmx fragments.
- `src/zibou/static/htmx.min.js`: htmx 2.0.11, vendored after checking the npm integrity hash. No CDN.
- `tests/test_zibou.py`: pytest with the Flask test client.

## Commands

```bash
. .venv/bin/activate                     # venv already exists on the server
ruff check . && ruff format --check .    # CI runs both
pytest -q
flask --app "zibou:create_app()" run --debug   # http://127.0.0.1:5000
```

`git push origin main` triggers CI, which pushes the image; production updates within 5 minutes.

## Conventions

- Config comes from `ZIBOU_*` environment variables (`app.config.from_prefixed_env("ZIBOU")`).
- In production the signed-in user arrives as the `X-Forwarded-Email` header from oauth2-proxy.
  It is only trustworthy because zibou has no published port. The app does not read it yet;
  the planned design is a `before_request` hook with a local-only `ZIBOU_DEV_USER` fallback.
- Keep the htmx pattern: routes return full pages or small fragments rendered by Jinja
  (autoescaped), not JSON, except `/health`.
- The image runs as uid 10001; anything persistent (e.g. a SQLite file) needs a mounted volume
  owned by that uid, because Watchtower recreates the container on every update.
