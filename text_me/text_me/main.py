from aiohttp import web

import aiohttp_jinja2
import jinja2

import logging

from .routes import setup_routes
from .settings import config, BASE_DIR


def run() -> None:
    logging.basicConfig(level=logging.DEBUG)
    app = web.Application()
    app["config"] = config
    print(BASE_DIR)
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(str(BASE_DIR / "templates"))
    )
    setup_routes(app)
    web.run_app(app)
