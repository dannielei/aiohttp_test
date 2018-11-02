#dannie  2018/9/17  17:39  PyCharm
import asyncio
from template import render_graphiql
from graphql_ws.aiohttp import AiohttpSubscriptionServer
from aiohttp import web
import json
from functools import partial
from schema_2 import schema_2
from graphql import  format_error

async def graphql_view(request):
    payload = await request.json()
    response = await schema_2.execute(payload.get('query', ''), return_promise=True)
    data = {}
    if response.errors:
        data['errors'] = [format_error(e) for e in response.errors]
    if response.data:
        data['data'] = response.data
    jsondata = json.dumps(data, )
    return web.Response(text=jsondata, headers={'Content-Type': 'application/json'})

async def graphiql_view(request, subscriptions_endpoint):
    return web.Response(text=render_graphiql(subscriptions_endpoint), headers={'Content-Type': 'text/html'})

subscription_server = AiohttpSubscriptionServer(schema_2)
async def subscriptions(request):
    ws = web.WebSocketResponse(protocols=('graphql-ws',))
    await ws.prepare(request)
    await subscription_server.handle(ws)
    return ws

async def init(loop):
    app = web.Application(loop=loop)

    app.router.add_get('/subscriptions', subscriptions)
    app.router.add_get('/graphiql', partial(graphiql_view, subscriptions_endpoint='ws:/192.168.1.44:8080/subscriptions'))
    app.router.add_get('/graphql', graphql_view)
    app.router.add_post('/graphql', graphql_view)

    srv = await loop.create_server(app.make_handler(), '192.168.1.44', 8080)
    print('Server started at http://192.168.1.44:8080/graphiql')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

# graphql_ws+ 异步IO + aiohttp + graphene
#python -m aiohttp.web -P 8080 aiohttp_query:init