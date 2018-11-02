#dannie  2018/9/13  17:36  PyCharm
from aiohttp import web
from aiohttp import web
import threading
import asyncio

# def get_all_todos(request):
#     return web.json_response('hw')
#
# def app_factory(args=()):
#     app = web.Application()
#     app.router.add_get('', get_all_todos)
#     return app
# python -m aiohttp.web -P 8080 text3:app_factory

import asyncio
from aiohttp import web

async def index(request):
    return web.json_response('1')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/index', index)
    srv = await loop.create_server(app.make_handler(), '192.168.1.138', 8080)
    print('Server started at http://192.168.1.138:8080/index')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

#异步IO+aiohttp
#python -m aiohttp.web -P 8080 text3:init