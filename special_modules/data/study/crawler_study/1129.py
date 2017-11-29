from urllib import request
from urllib import parse

'''
response = request.urlopen('http://www.baidu.com')
# print(response.read())
print(response.geturl())
print(response.getcode())
print(response.reason)

req = request.Request('https://docs.python.org/3/library/urllib.request.html#module-urllib.request', method='GET')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
print(req.full_url)
print(req.type)
print(req.host)
print(req.origin_req_host)
print(req.selector)
print(req.data)
'''
print(parse.urlparse('http://www.baidu.com'))
print(parse.urlsplit('http://www.baidu.com'))
print(parse.urljoin('http://www.baidu.com', 's?wd=python%20爬虫&rsv_spt=1&rsv_iqid=0x90a144fd0000ebc4&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsp=0&rsv_sug9=es_2_0&rsv_sug4=1019&rsv_sug=9'))