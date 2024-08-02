from urllib import request
from urllib import parse
import urllib
import socket
import urllib.error

try:
    rs = request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')


resp = request.urlopen(url='http://www.baidu.com')
# print(resp.read().decode('utf-8'))

data = bytes(parse.urlencode({"world":"hello"}),encoding='utf-8')
# print(data)#b'world=hello'

response = request.urlopen('http://httpbin.org/post',data=data)
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "world": "hello"
#   }, 
#   "headers": {
#     "Accept-Encoding": "identity", 
#     "Content-Length": "11", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "Python-urllib/3.11", 
#     "X-Amzn-Trace-Id": "Root=1-66aaeee2-3c3e11de4decb8416077094c"
#   }, 
#   "json": null, 
#   "origin": "119.131.119.207", 
#   "url": "http://httpbin.org/post"
# }
# print(response.read().decode('utf-8'))

result = request.urlopen('http://httpbin.org/get',timeout=1)

# b'{\n  "args": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.11", \n    "X-Amzn-Trace-Id": "Root=1-66aaef60-6c4c299867f4e42a5badec18"\n  }, \n  "origin": "119.131.119.207", \n  "url": "http://httpbin.org/get"\n}\n'
# print(result.read())




