import logging
logging.basicConfig(level=logging.INFO)

import asyncio, orm
from aiohttp import web
from models import User, Blog, Comment

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


async def test(loop):
    await orm.create_pool(user='root', password='Zdw*890412', database='awesome', loop=loop)
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_until_complete(test(loop))
loop.run_forever()