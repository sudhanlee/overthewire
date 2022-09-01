#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"
url = "http://%s.natas.labs.overthewire.org" % username

req_get = req.get(url,auth=(username,password))

# print(req_get.text)

nxt_pass = re.findall("<!--The password for natas2 is (.*) -->",req_get.text)
print(nxt_pass[0])