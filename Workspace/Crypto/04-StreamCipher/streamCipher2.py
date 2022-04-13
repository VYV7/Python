print("###############################################################################")
# A stream cipher is like a One Time Pad 
# No requirements on key stream hence not true randomness
# key stream can be reused
# Examples:
# - A5/1 (G2 encryption) - 54 bits
# - A5/2 (export version) - 17 bits
# - RC4 (WEP, SSL) - 40-2048 bits
# (algorithms kept secret)
# Challenges:
# - authenticity - MAC
# - reuse key
# - low entropy
print("1----------------------------------------------------")
print("implementation of stream cipher")
# the key cannot be true random because 
# the receiver must be able to regenerate it on their side

# generate key with linear congruential generator
# Xn+1 = (aXn + c) mod M
# starting with the same seed you always get the same sequence
# https://en.wikipedia.org/wiki/Linear_congruential_generator

import random

class keyStream:
	def __init__(self, key=1):
		self.next = key
		
	def rand(self):
		# formula implementation - returns a cipher
		# a = 1103515245, Xn = self.next , c = 12345
		self.next = (1103515245 * self.next + 12345) % 2**31
		return self.next
		
	def getKeyByte(self):
		# return a value between 0 and 255
		return self.rand() % 256
		
		
#----------------------------------------------------------		
def encrypt(key, message):
	# XOR all message bytes with a stream of random bytes
	return bytes([message[i] ^ key.getKeyByte() for i in range(len(message))])
	
#----------------------------------------------------------	
# simulation of transmition with losses (replacing random bytes in the cipher)
def transmit(cipher, likely):
	b = []
	for c in cipher:
		if random.randrange(0, likely) == 0:
			print("-- Transmission: changing cipher byte --")
			c = c ^ 2**random.randrange(0, 7)
		b.append(c)
	return bytes(b)
		
###############################################################################

key = keyStream()
message = "Hello world".encode()		# convert into byte object
print("Origianl message:\n", message)
cipher = encrypt(key, message)
print("Cipher:\n", cipher)


cipher = transmit(cipher, 7)
print("Changed cipher:\n", cipher)


key = keyStream()
decMsg = encrypt(key, cipher)
print("Decrypted message:\n", decMsg)

 







print("###############################################################################")
