### Heavens Flow
This challenge is very similar to the previous one, but this time we don't have `NX enabled`, so we can't use a shellcode on the stack since it's not executable. However, we can still overwrite the `return pointer` to execute the `heavens_secret` function, which will allow us to read the flag.
