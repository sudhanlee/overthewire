# BANDIT


### Level 0

**Username** : bandit0  
**Password** : `bandit0`

`ssh bandit0@bandit.labs.overthewire.org`

<------------------------------------------------------------------------------------------------------------------->

### Level 0 - 1

****Username**** : bandit0  
**Password** : `bandit0`

`cat readme`

<------------------------------------------------------------------------------------------------------------------->

### Level 1 - 2

**Username** : bandit1  
**Password** : `NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL` 

`cat ./-`

<------------------------------------------------------------------------------------------------------------------->

### Level 2 - 3

**Username** : bandit2  
**Password** : `rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi`

`cat spaces\ in\ this\ filename`

<------------------------------------------------------------------------------------------------------------------->

### Level 3 - 4

**Username** : bandit3  
**Password** : `aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG`

`cat inhere/.hidden`

<------------------------------------------------------------------------------------------------------------------->

### Level 4 - 5

**Username** : bandit4  
**Password** : `2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe`

`file inhere/-*` **to find the text file**  
`cat inhere/-file07` 

<------------------------------------------------------------------------------------------------------------------->

### Level 5 - 6

**Username** : bandit5  
**Password** : `lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR`

`find ./* ! -executable -size 1033c -readable` **to find the correct file**  
`cat inhere/maybehere07/.file2`

<------------------------------------------------------------------------------------------------------------------->

### Level 6 - 7

**Username** : bandit6  
**Password** : `P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU`

`find / -size 33c -user bandit7 -group bandit6 2>>/dev/null` **to find the file**  
`cat /var/lib/dpkg/info/bandit7.**Password**`

<------------------------------------------------------------------------------------------------------------------->

### Level 7 - 8

**Username** : bandit7  
**Password** : `z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S`

`cat data.txt | grep millionth`

<------------------------------------------------------------------------------------------------------------------->

### Level 8 - 9

**Username** : bandit8  
**Password** : `TESKZC0XvTetK0S9xNwm25STk5iWrBvP`

`sort data.txt | uniq -u`

<------------------------------------------------------------------------------------------------------------------->

### Level 9 - 10

**Username** : bandit9  
**Password** : `EN632PlfYiZbn3PhVK3XOGSlNInNE00t`

`strings data.txt | grep "&===="`

<------------------------------------------------------------------------------------------------------------------->

### Level 10 - 11

**Username** : bandit10  
**Password**: `G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s`

`cat data.txt | base64 -d`

<------------------------------------------------------------------------------------------------------------------->

### Level 11 - 12

**Username** : bandit11  
**Password** : `6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM`

`cat data.txt | tr "A-Za-z" "N-ZA-Mn-za-m"`

<------------------------------------------------------------------------------------------------------------------->

### Level 12 - 13

**Username** : bandit12  
**Password** : `JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv`

Create a folder in /tmp and copy data.txt file there  
`cat data.txt | xxd -r > data`  
**These are used multiple times.**Replace name with your file and format required  

`mv <filename> <filename>.{gz,bz,tar}`  
`gzip -d <filename>`  
`bzip2 -d <filename>`  
`tar -xvf <filename>`  
Finally,  
`cat data8`  

<------------------------------------------------------------------------------------------------------------------->

### Level 13 - 14

**Username** : bandit13  
**Password** : `wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw`

Create a folder in /tmp and copy sshkey.private file there  

`chmod 600 sshkey.private`  
`ssh -i sshkey.private bandit14@localhost`

<------------------------------------------------------------------------------------------------------------------->

### Level 14 - 15

**Username** : bandit14  
**Password** : `fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq`

`cat /etc/bandit_pass/bandit14 | nc localhost 30000`

<------------------------------------------------------------------------------------------------------------------->

### Level 15 - 16

**Username** : bandit15  
**Password** : `jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt`


`openssl s_client -host localhost -port 30001`  
Paste **Password** of **bandit15**.

<------------------------------------------------------------------------------------------------------------------->

### Level 16 - 17

**Username** : bandit16  
**Password** : `JQttfApK4SeyHwDlI9SXGR50qclOAil1`

`nmap localhost -p31000-32000`  
This is the few open ports. By bruteforcing you'll get the correct port which is **31790**.  

`openssl s_client -host localhost -port 31790`  
The port gives you the ssh key for the next level. Follow the same steps of **Level 13 - 14**   

### Level 17 - 18

**Username** : bandit17  
**Password** : `VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e`

`diff *`

<------------------------------------------------------------------------------------------------------------------->

### Level 18 - 19

**Username** : bandit18  
**Password** : `hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`

`ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"`

<------------------------------------------------------------------------------------------------------------------->

### Level 19 - 20

**Username** : bandit19  
**Password** : `awhqfNnAbc1naukrpqDYcF95h7HoMTrC`

`./bandit20-do cat /etc/bandit_pass/bandit20`

<------------------------------------------------------------------------------------------------------------------->

### Level 20 - 21

**Username** : bandit20  
**Password** : `VxCazJaVykI6W36BkBU0mJTCM8rR95XT`

Open 2 ssh terminals of user bandit20  
In one termial  
`nc -lvp 1337`  
On the other connect to the port given in last command which is `1337`.  
`./suconnect 1337`  
Now paste the correct **Password** in **nc** terminal  

<------------------------------------------------------------------------------------------------------------------->

### Level 21 - 22

**Username** : bandit21  
**Password** : `NvEJF7oVjkddltPSrdKEFOllh9V1IBcq`

`cd /etc/cron.d/`  
There is a file `cronjob_bandit22`  
`cat cronjob_bandit22`  
There will be another file's name inside it...`/usr/bin/cronjob_bandit22.sh`  
`cat /usr/bin/cronjob_bandit22.sh`  
The **Password** for bandit22 is stored from a tmp file `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`  
`cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`  

<------------------------------------------------------------------------------------------------------------------->v

### Level 22 - 23

**Username** : bandit22  
**Password** : `WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff`

`cd /etc/cron.d/`  
There is a file `cronjob_bandit23`  
`cat cronjob_bandit23`  
There will be another file's name inside it...`/usr/bin/cronjob_bandit23.sh`  
which is a bash script  
The **Password** for bandit23 is stored from a tmp file,  
The correct file name can be indentified my finding `mytarget` variable in the script.  
By replacing `myname` with `bandit23` will lead us to correct file name  

`echo I am user bandit23 | md5sum | cut -d ' ' -f 1`  
Will give us `8ca319486bfbbc3663ea0fbe81326349`  

`cat /tmp/8ca319486bfbbc3663ea0fbe81326349`

<------------------------------------------------------------------------------------------------------------------->

### Level 23 - 24

**Username** : bandit23  
**Password** : `QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G`

In `/usr/bin/cronjob_bandit24` there will be script running.  
To get the write a script in `/var/spool/bandit24/`  

```bash
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/sudhanlee/pass.txt

```
Now create `/tmp/sudhanlee/pass.txt` with full permission  

`cat pass.txt`

<------------------------------------------------------------------------------------------------------------------->

### Level 24 - 25

**Username** : bandit24  
**Password** : `VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar`

create a script in `tmp` directory and save the pin combination and pass it as input to `nc`.  
```bash
#!/bin/bash

for i in {0000..9999}
do
	echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i"
done
```

`chmod +x script.sh && ./script.sh > pins.txt && nc localhost 30002 < pins.txt`

<------------------------------------------------------------------------------------------------------------------->

### Level 25 - 26

**Username** : bandit25  
**Password** : `p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d`

Reduce the screen size very small until you see `(more)`.  
`v`  
`:r /etc/bandit_pass/bandit26`

<------------------------------------------------------------------------------------------------------------------->

### Level 26 - 27

**Username** : bandit26  
**Password** : `c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1`

Create a shell in the `vi` editor of bandit26 by,  
`:set shell=/bin/bash`  
`shell`  
After getting shell follow **Level 19 - 20**  

<------------------------------------------------------------------------------------------------------------------->

### Level 27 - 28

**Username** : bandit27  
**Password** : `YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS`

`git clone "ssh://bandit27-git@localhost/home/bandit27-git/repo"` in `tmp`  
`cat repo/README`

<------------------------------------------------------------------------------------------------------------------->

### Level 28 - 29

**Username** : bandit28  
**Password** : `0ef186ac70e04ea33b4c1853d2526fa2`

`git log`  
`git show <commit>`

<------------------------------------------------------------------------------------------------------------------->

### Level 29 - 30

**Username** : bandit29  
**Password** : `bbc96594b4e001778eee9975372716b2`

`git branch -a`  
`git checkout -b remotes/origin/dev`  
`git show`

<------------------------------------------------------------------------------------------------------------------->

### Level 30 - 31 

**Username** : bandit30  
**Password** : `5b90576bedb2cc04c86a9e924ce42faf`

`cat .git/packed-refs`  
`git show <last hash>`

<------------------------------------------------------------------------------------------------------------------->

### Level 31 - 32

**Username** : bandit31  
**Password** : `47e603bb428404d265f59c42920d81e5`

`echo "May I come in?" > key.txt`  
`git add . -f`  
`git commit -m "done"`  
`git push`  

<------------------------------------------------------------------------------------------------------------------->

### Level 32 - 33

**Username** : bandit32  
**Password** : `56a9bf19c63d650ce78e6ec0354ee45e`

`$0`  
Which lead to `sh` shell.

<------------------------------------------------------------------------------------------------------------------->

### Level 33 - 34

**Username** : bandit33  
**Password** : `c9c3199ddf4121b10cf581a98d51caee`


<------------------------------------------------------------------------------------------------------------------->
