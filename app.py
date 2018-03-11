import logging 
import asyncio,os,json,time,datetime
#from aiohttp import web
import aiohttp.web
logging.basicConfig(level=logging.INFO)
def index(request):
    return aiohttp.web.Response(body=b'<h1>Awesome<h1>')
@asyncio.coroutine
def init(loop):
    app=aiohttp.web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9999)
    logging.info('server started at http://127.0.0.1:9999')
    return srv
loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()