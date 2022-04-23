print("=============================================================")
# g - generator
# p - modular (prime number)

# Alice and Bob have the same g and p
# Alice generates a random value "a" and sends (g^a mod p) to Bob
# Bob generates a random value "b" and sends (g^b mod p) to Alice

# Alice (g^b mod p)^a = (g^b)^a mod p = g^(ab) mod p
# Alice can calculate g^ab mod p

# Bob (g^a mod p)^b = (g^a)^b mod p = g^(ab) mod p
# Bob can also calculate g^ab mod p

# Eve (g^a mod p) AND (g^b mod p) - cant get the right key

import math
import random

def isPrime(num):
	#for i in range(2, num):
	for i in range(2, math.isqrt(num)):
		if num % i == 0:
			return False
	return True
	
def getPrime(size):
	while True:
		p = random.randrange(size, 2*size)		# get a prime number from the range size - 2x size
		if isPrime(p):
			return p
			
def isGenerator(g, p):
	for i in range(1, p - 1):
		if (g**i) % p == 1:
			return False
	return True
			
def getGenerator(p):
	for g in range(2, p):
		if isGenerator(g, p):
			return g

print("1----------------------------------------------")
print("Diffie-Hellman key exchange")


	
	
p = getPrime(1000)
g = getGenerator(p)
print("p = ", p)
print("g = ", g)


"""
https://crypto.stackexchange.com/questions/16196/what-is-a-generator
A generator of a finite group is a value g such that all elements of the group 
can be represented as g^k for some integer k. 
Another key of looking at it is that if we consider the sequence g,  g*g,  g*g*g,..., 
saying g is a generator means that all values in the group will appear somewhere in the sequence.

when it comes to Diffie-Hellman, generator is used in two slightly different meanings

1. a "generator" is defined to be an element that generates the entire group.
we say that g generates the entire group means gkmodp can take on any value between 1 and p−1.

2. we say that an element g "generates" a subgroup. 
That is, when we consider all the possible values gkmodp, those possible values also form a group , 
and it makes sense to consider the Diffie-Hellman operation over this subgroup. In this case, 
we may call g the "generator" (even if it doesn't generate the full group). 
Now, this doesn't denote anything special about g (because all elements generate some subgroup by this meaning), 
instead we call g the generator to denote that it's the element we have chosen to use.


"""


























print("=============================================================")
