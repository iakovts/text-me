from aiohttp import web

import aiohttp_jinja2

from .db import write_post


class IndexHandle(web.View):
    @aiohttp_jinja2.template("text_form.html")
    async def post(self) -> None:
        form = await self.request.post()
        inserted_id = await write_post(form)
        # import pdb; pdb.set_trace()
        raise web.HTTPFound(self.request.app.router["play_again"].url_for())

    @aiohttp_jinja2.template("text_form.html")
    async def get(self):
        return {}


@aiohttp_jinja2.template("play_again.html")
async def play_again(request):
    if request.method == "POST":
        location = request.app.router["index"].url_for()
        raise web.HTTPFound(location)
