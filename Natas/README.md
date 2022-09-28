# Natas

**Natas** is a part of **overthewire** series. \
It teaches the basics of serverside web-security.

## Note:

These Challenges were solved only using python3 and uploaded in 
[sudhanlee/overthewire/Natas](https://github.com/sudhanlee/overthewire/Natas/)

### Lets start Hacking!!!

## Natas 0-1:
* **Username : natas0**
* **Password : natas0**

* It is one of the easiest challenge. 
* Just by inspecting the elements of the page, you'll find the password of natas1. 
* But we will solve it using python3. Now I will explain you the default code used in the whole **natas** series.
From next challenge I will explain you the procedure.

##### Head part of the code:

```python3

import requests
import re

username = "natas0"
password = "natas0"
url = "http://%s.natas.labs.overthewire.org" % username

req = requests.Session()

```
This first part of is default code for this series. \
The code will be same for all the challenges except the username and the password beacuse it keeps changing for every level. \
We use **requests** module to connect to the website and started a session(req).

##### Body part of the code:

```python3

get_req = req.get(url , auth=(username,password))

content = get_req.text

```
This is the part where we script to beak the security of the website. 

##### Tail of the code:

```python3

password_new = re.findall('<!--The password for natas1 is (.*) -->', content)[0]
print(password_new)

```
This part is used to extract and print only the password as output. \
Here we use **re** module to find the seperate the password from the output of **get_req**

##### Note:
* Remember, I splited the above code as **Head**, **Body** and **Tail** for understanding purpose. 
* This whole parts combindly will give you the output.
* If you are not aware of **requests** module, then check [this](https://www.w3schools.com/python/module_requests.asp)

### Solution:
This script will **get** request from the given url and authenticate with username and password provided. \
The get requested **page source** will be stored in `content = get_req.text`. \
Now If you print the **content**. You'll find the password of **natas1**. \
To seperate the correct password from the content, we use **re** module **findall** function.

The password of natas1 is `gtVrDuiDfck831PqWsLEZy5gyDz1clto`.

**Challenge natas 0-1 Solved**
