# install necessary libs with
# pip install cryptography
print("========================================================================")
import hashlib
import base64
from cryptography.fernet import Fernet

print("1--------------------------------")
# The key for the encrypted message below is 
# the largest known Fermat Prime passed through 
# an SHA3_256 Hash. This number should be passed 
# as a byte string by placing a b'' in front of the string.
# largest Fermat prime: 65537 

# encrypted message
encMsg = b'gAAAAABaSsmdCFRxbqA6n-L0CMIMuhn26uGiIk5Wtx-V7wEPLBZYA67nGbNWyZziGyorwIlHqp3M5xrtzQj5tCab8XfBRCmdJXZYD1Fwp68AtD8WEMhblQ4I2DKDNFzqULH1DDETry3ptZnGZUgVo5gdDlnihqu1_oX-KboNpyRQ6J0DmeWTsm3L31btF_O6sX81rj3rBVI0qVuT7QdRT2burisQRnw5htA05llYgc1_fMkN_PSxCwY='

# get the key
key = hashlib.sha3_256()		# create a hash object
key.update(b"65537")			# make a hashed string
keyBytes = key.digest()			# hashed version of the number
print("The key is:\n", keyBytes)


print("\n2--------------------------------")
print("decryption\n")

# generate cipher
# To do that the secret key is required
fernetKey = base64.urlsafe_b64encode(keyBytes)
print("Fermat key:\n",fernetKey)
cipher = Fernet(fernetKey)	
decMsg = cipher.decrypt(encMsg)	# decrypt

print("Decrypted message is:\n", decMsg)

print("========================================================================")
