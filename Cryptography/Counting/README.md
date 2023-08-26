### Counting
Finally, this is the last challenge that my team solved. In this challenge, the service was encrypting messages using `RSA` with very minor differences (practically one bit) using the following code:
```py
...
    message = b'So far we had %03d failed attempts to find the token %s' % (counter, token)
    print(pow(bytes_to_long(message), key.e, key.n))
...
```
In this case, you can attempt a [Franklin–Reiter](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#Franklin%E2%80%93Reiter_related-message_attack) attack by brute-forcing the changed bit until the decrypted message from the attack contains the token you need to find. Once you've obtained the token, you can send it to the service to get the flag.
