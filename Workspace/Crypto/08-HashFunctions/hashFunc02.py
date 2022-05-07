print("=============================================================")
"""
Hash function is a function that takes an in put of any size 
and produces an output binary of a fixed size.
	- one way deterministic
	  given the same input, it will always produce the same output.
	  Input cannot be calculated based on the output.
	- the output is dependent on all input bits.
	  small change in the input produces huge differnece in the output.
	  It is not possible to use output to determine the input.
	- impossible to predict the output based on the input
Has functions are used in:
	- digital signature
	- shadow files (password files) - passwords are not stored, only their hashes
	- HMAC (hashed message authentication codes) 
	- make deterministic identifiers
	
Implementing hash functions is very difficult but Python has built in libraries that contain
hash functions	
https://docs.python.org/3/library/hashlib.html
	
"""

import hashlib

# XORs the first byte with 1
def modify(m):
	l = list(m)
	l[0] = l[0] ^ 1
	return bytes(l)

#==============================================================================	

# Alice -----------------------------------------------------------------------
# n e and d are generated with RSA 
print("Alice")
print("\tpublic key (e, n):\t 5 170171")
print("\tsecret key (d):\t\t 9677")
n = 170171
e = 5
d = 9677
msg = "Bob you are awesome".encode()
print("\tmessage:\t\t", msg)

# step 1:  hash the message
sha256 = hashlib.sha256()
sha256.update(msg)
hash = sha256.digest()
print("\thash:\t", hash)
hash = int.from_bytes(hash, "big") % n		# convert into integers and shrink it (%)
print("\thash int:\t\t", hash)

# step 2: encrypt the hash value RSA (use secret exponent d)
sign = hash**d % n							# nobody else can calculate this value
print("\tsignature (secret):\t", sign)

# step 3: send message with signature to Bob
print("\tMessage sent to Bob:\t", msg, sign)



# Eve -------------------------------------------------------------------------
# comment/uncomment to test 
#msg = modify(msg)							# She modifies the message



# Bob -------------------------------------------------------------------------
print("Bob")
print("\treceived message:\t", msg)

# step 1: calculate the hash value
sha256 = hashlib.sha256()
sha256.update(msg)
hashB = sha256.digest()
hashB = int.from_bytes(hashB, "big") % n	# convert into integers and shrink it (%)
print("\tcalculated hash:\t", hashB)

# step 2: verify the signature
verif = sign**e % n							# this should be the same as the calculated hashB
print("\tverification val.:\t", verif)
if (verif == hashB):
	print("\tVerisifation SUCCESSFULL")
else:
	print("\tVerisifation FAILED !!!")























print("=============================================================")