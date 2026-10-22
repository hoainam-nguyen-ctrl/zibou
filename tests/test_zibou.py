import pytest

from zibou import __version__, create_app


@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    return app.test_client()


def test_index(client) -> None:
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.mimetype == "text/html"
    assert b'hx-get="/hello"' in resp.data
    assert b"/static/htmx.min.js" in resp.data


def test_htmx_is_served(client) -> None:
    resp = client.get("/static/htmx.min.js")
    assert resp.status_code == 200
    assert b"htmx" in resp.data


def test_hello_default(client) -> None:
    resp = client.get("/hello")
    assert resp.status_code == 200
    assert b"Hello, world!" in resp.data


def test_hello_name(client) -> None:
    resp = client.get("/hello", query_string={"name": "  Zibou  "})
    assert b"Hello, Zibou!" in resp.data


def test_hello_escapes_html(client) -> None:
    resp = client.get("/hello", query_string={"name": "<script>alert(1)</script>"})
    assert b"<script>" not in resp.data
    assert b"&lt;script&gt;" in resp.data


def test_hello_truncates_name(client) -> None:
    resp = client.get("/hello", query_string={"name": "x" * 200})
    assert b"x" * 50 + b"!" in resp.data


def test_health(client) -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok", "version": __version__}


def test_unknown_route(client) -> None:
    assert client.get("/nope").status_code == 404
