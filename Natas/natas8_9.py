#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"
url = "http://%s.natas.labs.overthewire.org" % username


data = {"secret":"oubWYf2kBq","submit":"Submit"}
req_post = req.post(url,auth=(username,password),data=data)

# print(req_post.text)


nxt_pass = re.findall("The password for natas9 is (.*)",req_post.text)
print(nxt_pass[0])
