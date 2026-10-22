from zibou import __version__, hello


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_hello() -> None:
    assert hello() == "Hello, world!"
    assert hello("Zibou") == "Hello, Zibou!"
