print("=============================================================")
"""
HMAC (Message Authentication Code)
Both parties have a shared key. This is different then in RSA.
HMAC is used to authenticate messages. 
- Message and the key are together hashed. That gives the messages authentication code (MAC). 
- Message and MAC are send across the network.
- the receiver uses his key to calculate MAC and then compares it with the received MAC
To change the message you need to know the key so you can calculate MAC.


"""

import hashlib

def modify(m):
	l = list(m)
	l[0] = l[0] ^ 1
	return bytes(l)

#==============================================================================	

# shared key
secretKey = "secret key".encode()

# Alice
print("Alice")
msg = "hey Bob".encode()
sha256 = hashlib.sha256()
sha256.update(secretKey)			# both know the key
sha256.update(msg)
hmacA = sha256.digest()

print("\tmessage:\t", msg)
print("\tHMAC:\t\t", hmacA)



# Eve
print("Eve")
msg = modify(msg)
print("\tmod-ed message:\t", msg)



# Bob
print("Bob")
msgRec = msg
sha256 = hashlib.sha256()
sha256.update(secretKey)			# both know the key
sha256.update(msgRec)
hmacB = sha256.digest()

print("\trec. message:\t", msgRec)
print("\tBob's HMAC:\t", hmacB)		# both MACs match


print("=============================================================")