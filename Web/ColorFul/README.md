### Colorful
This challenge was notably different from the standard web challenges I'm familiar with, as it required knowledge of `AES` vulnerabilities in `ECB` mode.
In this case, the source code contained a particularly suspicious section of code:

```py
def parse(self, c):
    d = {}
    if c is None:
        return d
    for p in c.split("&"):
        try:
            k,v = p.split("=")
            if not k in d:
                d[k]=v
        except:
            pass
    return d

def new_session(self, r):
    id = secrets.token_hex(4)
    c = f"_id={id}&admin=0&color=ffff00&"
    return self._c(c)

def _c(self, v):
    try:
        v = v.encode()
        while len(v) % 16 != 0:
            v += b'\x41' 
        return AES.new(self.k,1).encrypt(v).hex()
    except:
        return None
```
After looking at this code for a while, I noticed that it was possible to easily encrypt arbitrary blocks that, if crafted correctly, could be mixed together to create a cookie with admin privileges.<br>
At this point, what I did was fill the portion of the cookie that I couldn't modify myself, `_id={id}&admin=0&color=` (where id is a string of 4 * 2 hexadecimal characters), with characters at the end to make its length divisible by 16 (in other words, full blocks). Then, I wrote `admin=1` in the next block. This way, I could shift the last block to the beginning and overwrite the original cookie to obtain the flag.
