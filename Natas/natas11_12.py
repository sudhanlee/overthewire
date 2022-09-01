#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"
url = "http://%s.natas.labs.overthewire.org" % username


req_get = req.get(url,auth=(username,password))
req.cookies.set("data","ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK")
req_get = req.get(url,auth=(username,password))
# print(req_get.text)


nxt_pass = re.findall("The password for natas12 is (.*)<",req_get.text)
print(nxt_pass[0])
