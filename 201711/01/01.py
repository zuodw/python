#encoding = utf-8
import functools
import logging
logging.basicConfig(level=logging.INFO)
import pdb


try:
	print('try')
	r = 10 / int('2')
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
except ValueError as e:
	print('except:', e)
else:
	print('No Erro')
finally:
	print('finnally...')
print('END')

class MyError(ValueError):
	pass

def foo(s):
	n = int(s)
	if isinstance(n, int):
		raise MyError('invalid value: %s' % n)
	return 10 / n

try:
	foo(0)
except MyError as me:
	print(me)

def foo(s):
	n = int(s)
	assert n != 0, 'error! n is zero'
	return 10 / n
def main():
	try:
		print(foo(0))
	except AssertionError as ae:
		# pdb.set_trace()
		logging.exception(ae)
main()
print('END')