# install necessary libs with
# pip install cryptography
print("========================================================================")
import hashlib

print("1--------------------------------")
#  available algos
print("\n", hashlib.algorithms_available)


print("\n2--------------------------------")
print("cryptographic hash example (SHA3 256)")
# with hashing you can't go back 
# from the hashed msg to the original msg
hashObj = hashlib.sha3_256()		# create a hash object
hashObj.update(b"Hello")			# make a hashed string
hashMsg = hashObj.hexdigest()		# hashed version of the message
print("\n", hashMsg)


print("\n3--------------------------------")
print("encryption")
from cryptography.fernet import Fernet

key = Fernet.generate_key()			# generate a key
print("\nGenerated key:\n", key)

cipher = Fernet(key)				# create a cipher
# encrypt msg with this cipher
encMsg = cipher.encrypt(b"This message is encrypted")
print("\nEncrypted message is:\n", encMsg)


print("\n4--------------------------------")
print("decryption\n")

# generate another cipher
# To do that the secret key is required
# The secure key must be given securely to the other user
cipher2 = Fernet(key)	

decMsg = cipher2.decrypt(encMsg)	# decrypt

print("Decrypted message is:\n", decMsg)


print("\n5--------------------------------")
print("custom key string - not recommended")

keyword = b"123"		# custom keyword string (byte string - b"text")
						# byte string is like char string but with bytes
print("\nCustom key:\n", keyword)
# use hashing to turn the key into hash base 64 that Fernet will be able to use
key = hashlib.sha3_256(keyword)

digest = key.digest()
print("\nHash base 64 format:\n", digest)

# encode to base 64th
import base64

fernetKey = base64.urlsafe_b64encode(digest)
print("\nBase 64th format:\n", fernetKey)

# create custom cipher
custCipher = Fernet(fernetKey)
print("\nCustom cipher:\n", custCipher)

# test custom cipher
# encpypt
encMgs = custCipher.encrypt(b"Message encrypted with custom cipher")
print("\nEncripted message:\n", encMgs)

# decrypt
decMsg = custCipher.decrypt(encMgs)
print("\nDecrypted message:\n", decMsg)



print("========================================================================")
