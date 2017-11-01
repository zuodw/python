#encoding=utf-8

def my_abs(*args):
	for arg in args:
		if arg >= 0:
			return arg
		else:
			return -arg
