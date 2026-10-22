import pytest

from zibou import __version__, create_app


@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    return app.test_client()


def test_index(client) -> None:
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello from zibou!"}


def test_health(client) -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok", "version": __version__}


def test_unknown_route(client) -> None:
    assert client.get("/nope").status_code == 404
