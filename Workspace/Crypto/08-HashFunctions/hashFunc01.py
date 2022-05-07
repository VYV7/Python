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

#==============================================================================	

msg1 = "This is a message".encode()	# returns encoded version of the string - class 'bytes'

print("message:\t", msg1)
print("type:\t\t", type(msg1))
print("length:\t\t", len(msg1))
print("\n")

# 1st hash of the msg1 ------------------------------------
print("First hash of the message")
sha256a = hashlib.sha256()			# create sha256 object
print("\tobject:\t", sha256a)

sha256a.update(msg1)
digest1 = sha256a.digest()
print("\tdigest1:", digest1)
print("\tlength:\t", len(digest1))


# 2nd hash of the msg1 - produces exectly the same output -
print("2nd hash of the same message is the same as first one")
sha256b = hashlib.sha256()			# create sha256 object
print("\tobject:\t", sha256b)

sha256b.update(msg1)
digest2 = sha256b.digest()
print("\tdigest2: ", digest2)
print("\tlength:\t", len(digest2))


# 3rd hash of the msg1 - produces exectly the same output -
print("3rd hash of the same message with one byte changed - completely different hash!")
msg2 = "This is a messagE".encode()	
print("\tnew message:\t", msg2)
sha256c = hashlib.sha256()			# create sha256 object
print("\tobject:\t", sha256c)

sha256c.update(msg2)
digest3 = sha256c.digest()
print("\tdigest3: ", digest3)
print("\tlength:t", len(digest3))


def modify(m):
	list = list(m)
	list[0] = list[0] ^ 32
	return bytes(list)













print("=============================================================")