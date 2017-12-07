import logging
logging.basicConfig(level=logging.INFO)

import asyncio
from aiohttp import web

'''
定义'/'所需处理函数，request是浏览器自动发送过来的，不用自己定义
返回web.Response对象
'''
def index(request):
    return web.Response(body=b'<h1>Hello World</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), host='127.0.0.1', port=9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv



loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()