#encoding=utf-8

from urllib import request, parse

# req = request.Request('http://www.baidu.com')
# res = request.urlopen(req)
# print(res.read().decode('utf-8'))


# with request.urlopen('http://www.baidu.com') as f:
#     print(f.read().decode('utf-8'))


DATA = b'some data'
req = request.Request(url='http://www.baidu.com', data=DATA, method='PUT')
with request.urlopen(req) as f:
    pass
print(f.status, f.reason)

values = {'username':'836617785@qq.com', 'password':'XXX'}
data = parse.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
req = request.Request(url, data.encode('utf-8'))
res = request.urlopen(req)
print(res.read())