#!/usr/bin/python3.8

import requests
import meraki
import json
from pprint import pprint


version = "v1"
url='https://api.meraki.com/api/'+ version + '/organizations'

querystring= {}
header ={
    'X-Cisco-Meraki-API-Key': '9db387682aabec72abd403510cc1584db84fc34b'
}

response = requests.request("GET", url, headers=header)
print(response)
print("\n")
print(response.text.encode('utf8'))
print("\n")

# add json and pprint
responseJSON = json.loads(response.text)
pprint(responseJSON,indent=1,width=5)
print("\n")

#iterate

return_information = json.loads(response.text)
for x in return_information:
    print("ID: {} \nName: {} \nURL:{}\n ".format(x["id"],x["name"],x["url"]))
