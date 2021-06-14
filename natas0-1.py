#/usr/bin/env python3

import requests
import re

username = "natas0"
password = "natas0"
url = "http://%s.natas.labs.overthewire.org" % username

req = requests.Session()

get_req = req.get(url , auth=(username,password))

content = get_req.text

password_new = re.findall('<!--The password for natas1 is (.*) -->', content)[0]
print(password_new)