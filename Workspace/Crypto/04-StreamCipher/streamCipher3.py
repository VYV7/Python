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
	
#----------------------------------------------------------	
# cipher modification
# Simple example:
# original message: A = 0x41 = 01000001b
# encryption key:		0xAA = 10101010b
# encryption:			xor  = 11101011 (cipher)

# attacker's mod:	A -> P = 0x50 = 01010000b
# step 1 - A xor P:				A 	01000001b
#								P 	01010000b
#								xor	00010001b	
# step 2 - cipher xor step 1:		00010001b (A xor P)
#									11101011b (cipher)
#								xor	11111010b (new cipher)
# verify - new cipher xor key:		11111010b (new cipher)
#							0xAA	10101010b (key)
#								xor 01010000b (0x50 = P)

def mod(cipher):
	newCipher = [0]*len(cipher)				# create a list of the cipher's length
	# change some of the characters in the message
	newCipher[11] = ord("1") ^ ord("7")		# ord() takes a character and returns  its encoding
	
	return bytes([newCipher[i] ^ cipher[i] for i in range(len(cipher))])
	
		
###############################################################################

# Alice
key = keyStream(10)							# Alice's key
message = "Send Bob: $10".encode()		# convert into byte object
print("\nOrigianl message:\n", message)

cipher = encrypt(key, message)				# Alice encrypts the message
print("\nCipher:\n", cipher)

# stream cipher does not provide authenticity (digital signature)!
# the receiving end does not know if the message 
# has been sent by the trusted sender

# Bob amends the original message
print("\nBob sees only the cipher:\n", cipher)
cipher = mod(cipher)						# Bob modifyies the cipher

# Bank
key = keyStream(10)
decMsg = encrypt(key, cipher)
print("\nBank (decrypted message):\n", decMsg)

 







print("###############################################################################")
