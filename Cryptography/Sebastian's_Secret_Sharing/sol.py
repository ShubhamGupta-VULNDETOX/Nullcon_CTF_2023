#!/usr/bin/env python3
from pwn import remote
from Crypto.Util.number import long_to_bytes

r = remote("52.59.124.14", 10031) # the flag is in self.a[0] so we give self.n wich mod self.n is 0

r.recvuntil(b"N=")
N = int(r.recvuntil(b" ").decode().strip())
r.recvuntil(b"a share: ")
r.sendline(str(N).encode())
r.recvuntil(b"'")
flag = r.recvuntil(b"'").decode().strip().replace("'", "")
print(long_to_bytes(int(flag)).decode()) # ENO{SeCr3t_Sh4m1r_H4sh1ng}