import requests
import json
from requests.auth import HTTPBasicAuth

url1 = "https://192.168.135.129:8089/services/search/jobs/1672194359.2779/acl"
data = {"eai:acl.perms.read": ["123"]}
print(data)
json_data = json.dumps(data)
r = requests.post(
    url1, data=json_data, verify=False, auth=HTTPBasicAuth("admin", "Admin@123!")
)
# print (r)
get = requests.get(url1, verify=False, auth=HTTPBasicAuth("admin", "Admin@123!"))
print((get.text))
