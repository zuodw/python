#encoding=utf-8
from urllib import request

with request.urlopen('http://fantasy.wifigolf.com/index.php?clpga=20171011128&code=011nFfG01hhk002VdyG01TloG01nFfG0&state=clpga') as f:
	data = f.read()
	print('Status: ', f.status, f.reason)
	for key,value in f.getheaders():
		print('%s %s' % (key, value))
	print('Data:', data.decode('utf-8'))