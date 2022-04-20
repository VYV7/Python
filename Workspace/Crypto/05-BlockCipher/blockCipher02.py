# stream cipher takes plaintext and a key and xor it to get the cipher
# block cipher takes a block of plaitext and produces cipher block. 
# A key is used to encrypt
# 1 block is 8 bytes
# if a block is less than 8 bytes then the algo padds it

from pyDes import *

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
message = "0123456789ABCDEF0123456789ABCDEF"
key = "DESCRYPT"
iv = bytes([0]*8)
#k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)		# Electronic Codebook (ECB) mode decryption
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)		# Cipher Block Chaining (CBC) mode decryption
print("Message:\t\t", message)


# Alice sending the encrypted message
cipher = k.encrypt(message)
print("Length of plain text: ", len(message))
print("Length of cipher text: ", len(cipher))
print("Encrypted: \t\t", cipher[0:8])
print("Encrypted: \t\t", cipher[8:16])
#print("Encrypted: ", cipher[16])


# Bob modidying the encrypted message (cipher text)
# changine 1 bit in a block destroys the message
cipher = modify(cipher)
print("Encrypted (mod): \t", cipher[0:8])
print("Encrypted (mod): \t", cipher[8:16])


# Bank: decrypted message
message = k.decrypt(cipher)
print("Decrypted: ", message)
