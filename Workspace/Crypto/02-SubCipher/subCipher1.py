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
	
def encrypt(key, message):
	encMsg = ""
	for letter in message:
		if letter in key:
			encMsg += key[letter]
		else:
			encMsg += letter
	return encMsg
	
###############################################################################

message = "TEST MESSAGE"
print("Original message: \n", message)
key = genKey()
print("Key :\n", key)


encMsg = encrypt(key, message)
print("Encrypted message:\n", encMsg)

print("###############################################################################")
