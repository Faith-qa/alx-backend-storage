# 0x01.NOSQL
 | Short Specializations > Back-end > Storage |
 | ------------------------------------------ |
 | By Emmanuel Turlay, Staff Software Engineer at Cruise and Guillaume, CTO at Holberton school |
 | ------------------------------------------- |
 | Ongoing project - started 08-02-2021, must end by 08-04-2021 (in about 11 hours) - you're done with 0% of tasks. |
 | ------------------------------------------ |
 | Checker was released at 08-03-2021 06:00 AM |
 | ------------------------------------------ |
 | QA review fully automated. |

 # Resources
 Read or watch:

   * [NoSQL Databases Explained](https://alx-intranet.hbtn.io/rltoken/wweK7dOY4pf8haCqv9Iv6Q)
    * [What is NoSQL ?](https://alx-intranet.hbtn.io/rltoken/QqqNmgzgwopHBv305ki6bg)
    * [Building Your First Application: An Introduction to MongoDB](https://alx-intranet.hbtn.io/rltoken/vQl-gYKhCJH7vV3yM7c4dw)
    * [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://alx-intranet.hbtn.io/rltoken/9__3tR-NimgXlmjPQwTF-Q)
    * [Aggregation] (https://alx-intranet.hbtn.io/rltoken/5wocKNzm6MSQyHrFad1fZw)
    * [Introduction to MongoDB and Python](https://alx-intranet.hbtn.io/rltoken/axwwF4CjO7FnK8Ecochqnw)
    * [mongo Shell Methods](https://alx-intranet.hbtn.io/rltoken/CK-PTdRSbTqTeLqfo43v8A)
    * [The mongo Shell](https://alx-intranet.hbtn.io/rltoken/GT5RGf-0pRR_I5FYpw7sQg)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/HqF5KEIpyc_9oyWBN47Pww), without the help of Google:

## General
* What NoSQL means
* What is difference between SQL and NoSQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB

# Requirements
## MongoDB Command File
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
* All your files should end with a new line
* The first line of all your files should be a comment: // my comment
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc
## Python Scripts
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* Your code should use the ```pycodestyle style``` (version 2.5.*)
* The length of your files will be tested using ```wc```
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
* Your code should not be executed when imported (by using if __name__ == "__main__":)
# More Info
## Install MongoDB 4.2 in Ubuntu 18.04
[Official installation guide](https://alx-intranet.hbtn.io/rltoken/NsSPUtCi8ilcou6wofRu1Q)
```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```
Potential issue if documents creation doesn’t work or this error: ```Data directory /data/db not found., terminating (source and source)```

``` $ sudo mkdir -p /data/db```
Or if ```/etc/init.d/mongod``` is missing, please find here an example of the file:

Click to expand/hide file contents
## Use “container-on-demand” to run MongoDB
* Ask for container Ubuntu 18.04 - MongoDB
* Connect via SSH
* Or via the WebTerminal
* In the container, you should start MongoDB before playing with it:
```
$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$
```

# Tasks
| 0.List all databases |
| write a script that lists all databases in MongoDB.
```
guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
``` |

| create a database |
| Wrtie a script that creates or uses ```my_db```:

``` guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
guillaume@ubuntu:~/0x01$ cat 1-use_or_create_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
guillaume@ubuntu:~/0x01$
``` |

| 2. insert document |
| Write a script that inserts a document in the collection ```school```:

* The document must have one attribute name with value “Holberton school”
* The database name will be passed as option of mongo command 

```
guillaume@ubuntu:~/0x01$ cat 2-insert | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
guillaume@ubuntu:~/0x01$
``` |

| 3.All documents |
| Write a script that lists all documents in the collection ```school```:

    * The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 3-all | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```
|

| 4. All matches |
| Write a script that lists all documents with  name="Holberton school" in the collection school:

    * The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```
|
