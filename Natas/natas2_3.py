#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"
url = "http://%s.natas.labs.overthewire.org" % username

req_get = req.get(url+"/files/users.txt",auth=(username,password))

# print(req_get.text)

nxt_pass = re.findall("natas3:(.*)",req_get.text)
print(nxt_pass[0])