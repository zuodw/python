#encoding=utf-8
import random

""" 为了学习协程，复习生成器（generator） """
'''
def myGenerator():
	value = 0
	while True:
		receive = yield value
		if receive == 'quit':
			break
		value = 'got: %s' % receive


mg = myGenerator()
print(mg.send(None))
print(mg.send(5))
# print(mg.send('quit'))
mg.close()
'''

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)