from aiohttp.web import Application

from views import index

def setup_routes(app: Application) -> None:
    app.router.add_get("/", index)

