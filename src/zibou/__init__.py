"""Zibou Flask application."""

from flask import Flask, jsonify

__version__ = "0.1.0"


def create_app(config: dict | None = None) -> Flask:
    """Application factory."""
    app = Flask(__name__)
    app.config.from_prefixed_env("ZIBOU")
    if config:
        app.config.update(config)

    @app.get("/")
    def index():
        return jsonify(message="Hello from zibou!")

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=__version__)

    return app
