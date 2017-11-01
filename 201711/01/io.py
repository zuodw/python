#encoding = utf-8
from io import StringIO
from io import BytesIO

try:
	f = open('/code/git/201711/01/test.txt', 'r')
	str = f.read()
	print(str)
except IOError as e:
	print(e)
finally:
	if f:
		f.close()

""" 每次读完文件后，就到末尾了，所以不能连续使用read类的方法，应该有某种操作把文件指针移动到首位置 """
with open('/code/git/201711/01/test.txt', 'r', encoding='gbk', errors='ignore') as f:
	print(f.read())
	# print(f.read(8))
	# for line in f.readlines():
	# 	print('zzzzz')
	# 	print(line)

with open('test.txt', 'w') as f:
	f.write('zuodw\n')
	f.write('fanhx\n')

""" StringIO """
f = StringIO()
print(f.write('Hello World'))
print(f.getvalue())


f = BytesIO()
f.write('中国'.encode('utf-8'))
print(f.getvalue())

fh = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(fh.read())