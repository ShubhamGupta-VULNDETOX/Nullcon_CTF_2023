### Babypwn
Finally, a bit of pwn. This challenge included an `ELF` file as an attachment. Running `checksec` to examine it yielded the following responses:
```
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX disabled
PIE:      No PIE (0x400000)
RWX:      Has RWX segments
```
At this point, it's enough to examine it with IDA, where you have a buffer of `512` characters available and a read function that reads `1024` characters. 
```c
...
   char username[512];

   printf("You shell play a game against @gehaxelt! Win it to get ./flag.txt!\n");
   printf("Your game slot is at: %p\n", username);
   printf("What's your name?\n");
   read(1, username, 1024);
...
```
This allows us to perform a `buffer overflow`. We can fill the buffer with a shellcode at the beginning, followed by multiple 'a' characters to fill the remaining space in the buffer. Once the buffer is filled, we just need to overwrite the `RBP` register and then the `return pointer` with the address of the shellcode. This way, we can execute a shell on the remote machine.
