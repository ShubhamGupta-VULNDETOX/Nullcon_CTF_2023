#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import sys
import os
from secret import flag

MAX_COUNT = 128

key = RSA.generate(2048, e = 1337)
token = os.urandom(len(flag))

def loop():
	print('My public modulus is:\n%d' % key.n)
	print('Let me count how long it takes you to find the secret token.')

	for counter in range(MAX_COUNT):
		message = b'So far we had %03d failed attempts to find the token %s' % (counter, token)
		print(pow(bytes_to_long(message), key.e, key.n))
		print('What is your guess?')
		sys.stdout.flush()
		guess = sys.stdin.buffer.readline().strip()
		if guess == token:
			print('Congratulations for finding the token after %03d rounds. Here is your flag: %s' % (counter, flag))
			sys.stdout.flush()
			return
	print('Nope! No more attempts.')

if __name__ == '__main__':
	try:
		loop()
	except Exception as err:
		print('encountered some error')
