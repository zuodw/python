#encoding = utf-8

from urllib import request

with request.urlopen('http://fantasy.wifigolf.com/index.php?clpga=20171011128') as f:
    data = f.read()
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s, %s' % (k, v))