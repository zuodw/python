#/usr/bin/python
#encoding: utf-8

' sub functions modules '

__author__ = 'zuodw'

def sub_add(*args):
	sum = 0
	for x in args:
		sum = sum + x
	return sum