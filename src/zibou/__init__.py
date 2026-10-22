"""Zibou Flask application."""

from datetime import datetime

from flask import Flask, jsonify, render_template, request

__version__ = "0.1.0"

MAX_NAME_LENGTH = 50


def create_app(config: dict | None = None) -> Flask:
    """Application factory."""
    app = Flask(__name__)
    app.config.from_prefixed_env("ZIBOU")
    if config:
        app.config.update(config)

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/hello")
    def hello():
        """HTML fragment swapped into the page by htmx."""
        name = request.args.get("name", "").strip()[:MAX_NAME_LENGTH] or "world"
        return render_template("_greeting.html", name=name, now=datetime.now())

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=__version__)

    return app
