# substitution cipher maps letters to any of the unsued letters in the alphabet
# that gives billions of permutations (26!)
print("###############################################################################")
import random

def genKey():
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cletters = list(letters)
	key = {}
	for letter in letters:
		key[letter] = cletters.pop(random.randint(0, len(cletters)-1))
	return key

# this is the same as in case of the Caesar cipher
def encrypt(key, message):
	encMsg = ""
	for letter in message:
		if letter in key:
			encMsg += key[letter]
		else:
			encMsg += letter
	return encMsg

# this is the same as in case of the Caesar cipher
# create the reverse key
def get_decript_key(key):
	dkey = {}
	for k in key:
		dkey[key[k]] = k
	return dkey
	
	
###############################################################################

message = "TEST MESSAGE"
print("Original message: \n", message)
key = genKey()
print("Key :\n", key)


encMsg = encrypt(key, message)
print("Encrypted message:\n", encMsg)


dkey = get_decript_key(key)
message = encrypt(dkey, encMsg)
print("Decripted message:\n", message)





print("###############################################################################")
