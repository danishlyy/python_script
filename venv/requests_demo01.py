import requests

url = 'http://httpbin.org/get'
data = {'key':'value','abc':'xyz'}
response = requests.get(url,data)
# {
#   "args": {
#     "abc": "xyz", 
#     "key": "value"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate, br, zstd", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.3", 
#     "X-Amzn-Trace-Id": "Root=1-66ac9c2b-5bfdadb46efd20da22b8e75e"
#   }, 
#   "origin": "119.131.119.207", 
#   "url": "http://httpbin.org/get?key=value&abc=xyz"
# }
# print(response.text)


url = 'http://httpbin.org/post'
data = {'key':'value','abc':'xyz'}
response = requests.post(url,data)
# {'args': {}, 'data': '', 'files': {}, 'form': {'abc': 'xyz', 'key': 'value'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Content-Length': '17', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-66ac9c45-632dd5421f4a241a04c4d646'}, 'json': None, 'origin': '119.131.119.207', 'url': 'http://httpbin.org/post'}
print(response.json())
