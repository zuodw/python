#/usr/bin/python
#coding: utf-8
'a test module'
__author__ = 'zuodw'

from PIL import Image


'''
import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print("Hello World %s" % (args[0]))
	elif len(args) == 2:
		print("Hello %s" % (args[1]))
	else:
		print("too many arguments".title())

if __name__ == '__main__':
	test()

# im = Image.open('F:/code/git/python/1026/zuodw.jpg')
im = Image.open('zuodw.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200,100))
im.save('thumbnail.jpg', 'JPEG')

'''

print('面向对象编程, 类（class）和实例（instance）')

class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.score = score
	def print_name(self):
		print(self.__name)
fanhx = Student('fanhx', 100)
fanhx.__name = 'fhx'
print("a", fanhx.__name)
print("b", fanhx._Student__name)
zuodw = Student('zuodw', 99)
zuodw.__age = 29
zuodw.__age = 30
fanhx.print_name()
# print(fanhx.age)
print(zuodw.__age)