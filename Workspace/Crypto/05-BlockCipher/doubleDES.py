# stream cipher takes plaintext and a key and xor it to get the cipher
# block cipher takes a block of plaitext and produces cipher block. 
# A key is used to encrypt
# 1 block is 8 bytes
# if a block is less than 8 bytes then the algo padds it

from pyDes import *
import random

# #############################################################################
# changine 1 bit in a block destroys the message in ECB mode
def modify(cipher):
    mod = [0] * len(cipher)
    #mod[10] = ord(" ") ^ ord("1")
    #mod[11] = ord(" ") ^ ord("0")
    #mod[10] = ord("1") ^ ord("0")
    mod[8] = ord("G") ^ ord("T")
    return bytes(mod[i] ^ cipher[i] for i in range(len(cipher)))

# #############################################################################


#message = "Give Bob:  10$ and send them to him"
message = "01234567"
print("Message:\t", message)


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
cipher = k1.encrypt(k2.encrypt(message))					# double encryption
print("Key 11:\t", key_11)
print("Key 21:\t", key_21)
print("\nEncrypted:\n", cipher)



# Bob: decrypted message
decMsg = k2.decrypt(k1.decrypt(cipher))
print("Decrypted:\n", decMsg)


#Eve's attack on Double DES


