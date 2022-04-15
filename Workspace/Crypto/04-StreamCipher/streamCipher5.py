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
# - reuse key				<--
# - low entropy
print("1----------------------------------------------------")
print("Stream cipher - low entropy exploitation\n\n")

# the key cannot be true random because 
# the receiver must be able to regenerate it on their side

# generate key with linear congruential generator
# Xn+1 = (aXn + c) mod M
# starting with the same seed you always get the same sequence
# https://en.wikipedia.org/wiki/Linear_congruential_generator

import random

class keyStream:
	def __init__(self, key=1):
		self.next = key			# this is the seed
		
	def rand(self):
		# formula implementation - returns a cipher
		# a = 1103515245, Xn = self.next , c = 12345
		self.next = (1103515245 * self.next + 12345) % 2**31
		return self.next					# return a 32 bit integer
		
	def getKeyByte(self):
		# get a random number and
		# convert it into a value between 0 and 255
		#return self.rand() % 256			# return the LEAST significant byte
		
		# get a random number and
		# convert it into a value between 0 and 255
		# return self.rand() % (2**31)		# return a 32 bit integer
		
		# // is floor division, returns div result without fraction
		# take the top byte, shift it right by 3 bytes ???
		return (self.rand() // 2**23) % 256	# return the MOST significant byte		

		
		
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
	
#----------------------------------------------------------	
# the key can be extracted by xoring the message and the cipher	
def getKey(message, cipher):
	return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])
	
	
#----------------------------------------------------------	
def crack(keyStream, cipher):
	length = min(len(keyStream), len(cipher))
	return bytes([keyStream[i] ^ cipher[i] for i in range(length)])
	
	
#----------------------------------------------------------	
# goes through all possible key values until it gets t right
def bruteForce(plaintext, cipher):
	matchCnt = 0
	# scan all possible keys
	for key in range(2 **31):
		bfKey = keyStream(key)						# generate a key
		# xor plaintext with cipher to get a key
		for j in range(0, len(plaintext)):
			xorVal = plaintext[j] ^ cipher[j]		# calc Key based on plaintext XOR cipher
			if xorVal != bfKey.getKeyByte():		# check if the guessed key alignes with the calc key
				break
		else:
			#matchCnt += 1
			#if matchCnt == 3:
			return key
	return False
		
		
		
		
	
		
###############################################################################

# In cryptography, entropy refers to the randomness 
# collected by a system for use in algorithms
# that require random data
# A lack of good entropy can leave a cryptosystem vulnerable 
# and unable to encrypt data securely

# Stream Cipher uses the linear congruential generator





# Alice - sends the message
# secretKey = 10
secretKey = random.randrange(0, 2**20)
print("Secret key:\n", secretKey)
key = keyStream(secretKey)					# Alice's key

# usually messages have a defined structure.
# header is one part of the structure.
header = "MESSAGE: "

message = "MESSAGE: " + "My secret message to Bob"
message = message.encode()
print("\nMessage:\n", message)

cipher = encrypt(key, message)				# Alice encrypts the message
print("\nAlice - cipher 1:\n", cipher)


# Bob - receives the message (he's got the same key)
key = keyStream(secretKey)
decMsg = encrypt(key, cipher)
print("\n Bob: decrypted message:\n", decMsg)


# Eve *********************************
bfKey = bruteForce(header.encode(), cipher)		# header is the part of plaintext that Eve knows
print("\nEve's brute force key:\n", bfKey)	

key = keyStream(bfKey)
decMsg2 = encrypt(key, cipher)
print("Eve: decrypter message:\n", decMsg2)















print("###############################################################################")
