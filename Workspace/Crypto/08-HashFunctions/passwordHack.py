print("=============================================================")
"""

"""

import hashlib
import base64

# combines all possible combinations of 2 letters
# calculatees hash and compares it with the one that is known
def guessPassword(salt, iterations, entropy):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for c1 in alphabet:
		for c2 in alphabet:
			password = str.encode(c1 + c2)
			value = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128))
			if value == entropy:
				return password
	return "".encode()
			

#==============================================================================	
password = "pw".encode()		# let's imagine we dont know that password


# but we know this - can be fount on a machine fs?
iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
validation = "SALTED-SHA512-PBKDF2"
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
entropy = base64.b64encode(value)			# this value is stored on the machine

print("This is known")
print("\tvalue:\n", value)
print("\tentropy:\n", entropy)
print("\titerations:\t", iterations)
print("\tsalt:\t\t", salt)

# searching for password
print("\nThis is unknown")
passwordH = "??".encode()
print("\tpassword:\t", passwordH)



passwordH = guessPassword(salt, iterations, entropy)
valueH = hashlib.pbkdf2_hmac("sha512", passwordH, salt, iterations, dklen=128)
print("\n\thacked password:\t", passwordH)
print("\thacked value:\n", valueH)



print("=============================================================")