# 0x00. MySQL advanced
# Concepts

| For this project, students are expected to look at this concept:
..* [Advanced SQL](https://alx-intranet.hbtn.io/concepts/555) |

# Resources
Read or watch:
.. * [MySQL cheatsheet] (https://alx-intranet.hbtn.io/rltoken/8w9di_hk19DIMSBEV3EayQ)

.. * [MySQL Performance: How To Leverage MySQL](https://alx-intranet.hbtn.io/rltoken/2GJbZ48zRPA70o2YhTdH7g) 
..* [Database Indexing](https://alx-intranet.hbtn.io/rltoken/K180X2OCzb6gzPngjn-EIg)
.. * [Stored Procedure](https://alx-intranet.hbtn.io/rltoken/K180X2OCzb6gzPngjn-EIg)
.. * [Triggers](https://alx-intranet.hbtn.io/rltoken/cJ1qA4o-rRm4rWIsqYKSZg)
..* [Views](https://alx-intranet.hbtn.io/rltoken/vHg1z3UAOcWMvOt8xZHeiA)
..* [Functions and Operators](https://alx-intranet.hbtn.io/rltoken/g-c1m6iljScpi4LeqxBRqQ)
.. * [Trigger Syntax and Examples](https://alx-intranet.hbtn.io/rltoken/gLVwKjQfRL0Jr_nWqAS7VQ)
..* [CREATE TABLE Statement](https://alx-intranet.hbtn.io/rltoken/X789nJ22H6HVh1uCQPl0lg)
..* [CREATE PROCEDURE and CREATE FUNCTION Statements](https://alx-intranet.hbtn.io/rltoken/mfrWMt1KL3NHXblJykMgZg)
..* [CREATE INDEX Statement](https://alx-intranet.hbtn.io/rltoken/oCu8Rg9WfKyF4BhTt8dZGQ)
..* [CREATE VIEW Statement](https://alx-intranet.hbtn.io/rltoken/FEZNlZFKZmD1ISnLINkCwQ)

# Learning Objectives
At the end of the project, the leatner is expected to be able to explain to anyone, without helo of google:

## General
..* How to create tables with constraints
..* How to optimize queries by adding indexes
..* What is and how to implement stored procedures and functions in MySQL
..* What is and how to implement views in MySQL
..* What is and how to implement triggers in MySQL

# Requirements
## General
..* All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
..* All your files should end with a new line
..* All your SQL queries should have a comment just before (i.e. syntax above)
..* All your files should start by a comment describing the task
..* All SQL keywords should be in uppercase (SELECT, WHERE…)
..* A README.md file, at the root of the folder of the project, is mandatory
..* The length of your files will be tested using wc

# More info
## Comments for your SQL file:
| $ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$ |
|--------------------------------------------------|

# Tasks

| 0.We are all Unique |
| -------------------- |
| Write a SQL script that creates a table users following these requirements:

..* With these attributes:
    ..* id, integer, never null, auto increment and primary key
    ..* email, string (255 characters), never null and unique
    ..* name, string (255 characters)
..* If the table already exists, your script should not fail
..* Your script can be executed on any database

Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application 
| bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ |
|

| 1. In and not out |
| ----------------- |
| Write a SQL script that creates a table users following these requirements:

..* With these attributes:
    ..* id, integer, never null, auto increment and primary key
    ..* email, string (255 characters), never null and unique
    ..* name, string (255 characters)
    ..* country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
..* If the table already exists, your script should not fail
..* Your script can be executed on any database
| bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$ |
 |

 