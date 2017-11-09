#encoding=utf-8
from contextlib import contextmanager, closing
from urllib.request import urlopen

'''
class Query(object):
	def __init__(self, name):
		self.name = name

	def __enter__(self):
		print('enter')
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('exit')

	def query(self):
		print('Query info about ( %s )' % ( self.name ))

with Query('Bob') as b:
	b.query()

class Query(object):
	def __init__(self, name):
		self.name = name

	def query(self):
		print('Query info about ( %s )' % ( self.name ))

@contextmanager
def create_query(name):
	print('enter')
	q = Query(name)
	yield q
	print('exit')

with create_query('Bob') as q:
	q.query()
'''

with closing(urlopen('http://www.baidu.com')) as page:
	for line in page:
		print(line)