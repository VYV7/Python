print("=============================================================")
"""
Password is stored on a machne as a hashe of concatentaion of
a password and salt.

password entered by a user is hashed together with salt. Machine verifies hashes,
not the actual passwords.

PBKDF2 (Password-Bsed Key Derivation Function 2) is a key derivation function
used to reduce vulnerability to brute force attacks

PBKDF2 is implemented in hashlib
	
	
https://en.wikipedia.org/wiki/PBKDF2
"""

import hashlib
import base64

#==============================================================================	
# The same password but different salts
# sale ensures that the same passwords are stored in a different way
# result in diffrent values stored in machines

print("--- Alice ---")
iterations = 45454

# salt is unique to the user - otherwise the password hashed wouldbe the same !!!
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())

validation = "SALTED-SHA512-PBKDF2"
password = "password".encode()
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
entropy = base64.b64encode(value)			# this value is stored on the machine

print("\tvalue:\n", value)
print("\tentropy:\n", entropy)
print("\titerations:\t", iterations)
print("\tsalt:\t", salt)




print("\n--- Bob ---")
iterationsB = 45454

# salt is unique to the user - otherwise the password hashed wouldbe the same !!!
#salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
saltB = "123".encode()

passwordB = "password".encode()
valueB = hashlib.pbkdf2_hmac("sha512", password, saltB, iterations, dklen=128)
entropyB = base64.b64encode(valueB)			# this value is stored on the machine

print("\tvalue:\n", valueB)
print("\tentropy:\n", entropyB)
print("\titerations:\t", iterationsB)
print("\tsalt:\t", saltB)




print("=============================================================")