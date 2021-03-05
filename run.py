#teste gabriel braz - oystr
import urllib.request
import json
url = 'https://ipinfo.io/json'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request).read()
json_content = json.loads(response.decode('utf-8'))

print("----")
print("IP: ", json_content['ip'], " - City: ", json_content['city'])
print("----")