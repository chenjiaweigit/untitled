import requests
# ro1 = requests.get("https://www.baidu.com")com
# print( ro1.status_code)
import json


# payload = {'key1':'name','key2':'sex'}

# r1 = requests.get('http://httpbin.org/get',params = payload)
# print(r1.url) #获取请求内容
# print(r1.text)#获取相应内容

# r = requests.get('https://baidu.com')
# print(r.headers['Server'])


r = requests.get('http://httpbin.org/status/404')

print(r.status_code)