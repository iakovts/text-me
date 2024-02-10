import datetime
import json 
from typing import Any
from aiohttp import WSMsgType, web
import aiohttp
import aiohttp_jinja2

from .db import find_all, write_post


class IndexHandle(web.View):
    @aiohttp_jinja2.template("text_form.html")
    async def post(self) -> None:
        form = await self.request.post()
        inserted_id = await write_post(form)
        raise web.HTTPFound(self.request.app.router["play_again"].url_for())

    @aiohttp_jinja2.template("text_form.html")
    async def get(self):
        return {}


class FetchHandler(web.View):
    last_fetch = None
    async def get(self):
        resp = await find_all(FetchHandler.last_fetch)
        FetchHandler.last_fetch = datetime.datetime.now()
        return web.json_response(resp)



@aiohttp_jinja2.template("play_again.html")
async def play_again(request):
    if request.method == "POST":
        location = request.app.router["index"].url_for()
        raise web.HTTPFound(location)


async def websocket_handler(request):

        ws = web.WebSocketResponse()
        await ws.prepare(request)
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == "close":
                    await ws.close()
                else:
                    await ws.send_str(msg.data) 
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print("ws connection closed with error %s" % ws.exception())

