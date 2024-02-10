from aiohttp import web
from aiohttp.web import Application

from .views import FetchHandler, IndexHandle, play_again, websocket_handler
from .settings import BASE_DIR


def setup_routes(app: Application) -> None:
    app.router.add_post("/", IndexHandle, name="index")
    app.router.add_get("/", IndexHandle)
    app.router.add_get("/get_records", FetchHandler)
    app.router.add_get("/again", play_again, name="play_again")
    app.router.add_post("/again", play_again)
    app.router.add_static("/static/", path=BASE_DIR / "static", name="static")
