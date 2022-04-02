print("========================================================================")

print("1--------------------------------")
print("Hint from the coordinates:")
print("'KEY IS TRUTH'\n")

encMsg = b'gAAAAABaUXStIpjRWJTrbWGOB45IyRpbb8Zyl1sdktcSeOL0zpH-_Oxd2nXVjeph_fGybthCci75lTd0z5SycthFo-5uoFxZqeBTdDc_n9uq3FdZk75gYFAWIRSGlAqlBQlcqkNhVx3W3w7rTaCAhCrHijeyTtxq53S3ab6fLHUw3KPHx2LtdurISe5ArhrmG9IOepnzGzBBTaTgCfoAmbITCWbp_5cdQQ=='
print("Encrypted message:")
print(encMsg)


print("\n2--------------------------------")
print("decryption")

import hashlib
from cryptography.fernet import Fernet
import base64

keyword = b"TRUTH"					# custom keyword string (byte string - b"text")
key = hashlib.sha3_256(keyword)

keyBytes = key.digest()
print("\nHash base 64 format:\n", keyBytes)

fernetKey = base64.urlsafe_b64encode(keyBytes)
print("\nBase 64th format:\n", fernetKey)

cipher = Fernet(fernetKey)
print("\nCipher object:\n", cipher)


#encMgs = cipher.encrypt(b"Message encrypted with custom cipher")
#print("\nEncripted message:\n", encMsg)

# decrypt
decMsg = cipher.decrypt(encMsg)
print("\nDecrypted message:\n", decMsg)




print("========================================================================")
