# stream cipher takes plaintext and a key and xor it to get the cipher
# block cipher takes a block of plaitext and produces cipher block. 
# A key is used to encrypt
# 1 block is 8 bytes
# if a block is less than 8 bytes then the algo padds it

from pyDes import *
import random

print("====================================================================")

key_11 = random.randrange(0, 256)					# generate a random number 0-256
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])		# create 8 byte key
key_21 = random.randrange(0, 256)					# generate a random number 0-256
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])		# create 8 byte key

iv = bytes([0]*8)



# double DES (Data Encryption Standard)
#k1 = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)		# Cipher Block Chaining (CBC) mode decryption
k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)		# Electronic Codebook (ECB) mode decryption
k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)		# Electronic Codebook (ECB) mode decryption



# Alice sending the encrypted message
print("Alice")

message = "01234567"
print("Message:\t", message)

cipher = k1.encrypt(k2.encrypt(message))			# double encryption (cipher2)
print("Key 11:\t", key_11)
print("Key 21:\t", key_21)
print("Encrypted:\n", cipher)



# Bob: decrypted message
print("\nBob")
decMsg = k2.decrypt(k1.decrypt(cipher))				# double decryption
print("Decrypted:\n", decMsg)



# Eve's attack on Double DES
# Eve knows the message and cipher 2
# message -> cipher 1 -> cipher 2
# 1:	message -> cipher 1a
# 2:	cipher 1b <- cipher 2
# 3:	(cipher 1a == cipher 1b) ? valid keys
print("\nEve")
lookup = {}											# lookup table to store encrypted msgs

# create a dictionary with messages encrypted 
# with all possible keys - list of ciphers 1a
for i in range(256):
	key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
	k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
	lookup[k.encrypt(message)] = i					# each encrypted msg has a key assigned to it		

# decrypt cipher with all possible keys (cipher 1b)
# and check which one matches one of the 
# encrypted messages in the lookup table
# if it does, then she has the right 2 keys
for i in range(256):
	key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
	k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)	
	# decrypt cipher with each key and 
	# check if it matches an enc msg in the lookup table
	if k.decrypt(cipher) in lookup:					
		print("Hacked Key 11: ", i)							# print the key used for cipher 1b <- cipher 2
		print("Hacked Key 21: ", lookup[k.decrypt(cipher)])	# print the key used for message -> cipher 1a
		
		# create a set of keys
		key_1e = bytes([i, 0, 0, 0, 0, 0, 0, 0])
		key_2e = bytes([lookup[k.decrypt(cipher)], 0, 0, 0, 0, 0, 0, 0])
		
		k1e = des(key_1e, ECB, iv, pad=None, padmode=PAD_PKCS5)
		k2e = des(key_2e, ECB, iv, pad=None, padmode=PAD_PKCS5)
		
		# decrypt cipher 2
		decMsg2 = k2e.decrypt(k1e.decrypt(cipher))
		print("Decrypted message:\n", decMsg2)
		
		break





















print("====================================================================")

