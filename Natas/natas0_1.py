#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas0"
password = "natas0"
url = "http://%s.natas.labs.overthewire.org" % username

req_get = req.get(url,auth=(username,password))

nxt_pass = re.findall("<!--The password for natas1 is (.*) -->",req_get.text)
print(nxt_pass[0])