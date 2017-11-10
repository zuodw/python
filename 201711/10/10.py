#encoding=utf-8
import asyncio
import threading
'''
def customer():
    num = 0
    s = ''
    while True:
        num = yield s
        s = 'Customer ( %s )' % ( str(num) )
    
def prodece(c):
    c.send(None)
    for i in range(5):
        print('Produce ( %s )' % ( str(i) ))
        print(c.send(i))
    c.close()

c = customer()
prodece(c)
'''

'''
@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % (threading.currentThread()))
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again! (%s)" % (threading.currentThread()))

# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''

async def hello():
    print("Hello world! (%s)" % (threading.currentThread()))
    # 异步调用asyncio.sleep(1):
    r = await asyncio.sleep(1)
    print("Hello again! (%s)" % (threading.currentThread()))

# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
