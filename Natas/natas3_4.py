#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"
url = "http://%s.natas.labs.overthewire.org" % username

req_get = req.get(url+"/s3cr3t/users.txt",auth=(username,password))

# print(req_get.text)

nxt_pass = re.findall("natas4:(.*)",req_get.text)
print(nxt_pass[0])