from aiohttp.web import Application

from .views import IndexHandle, play_again


def setup_routes(app: Application) -> None:
    app.router.add_post("/", IndexHandle, name="index")
    app.router.add_get("/", IndexHandle)
    app.router.add_get("/again", play_again, name="play_again")
    app.router.add_post("/again", play_again)
