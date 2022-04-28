print("=============================================================")
# Diffie-Hellman key exchange
# establishes a common secret between two parties
# that can be used for secret communication for exchanging data 
# over a public network. See end of file for explanation
# https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

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
	#for i in range(2, num):					# don't use 0, 1 and num
	#for i in range(2, (int)(num/2)):			# composite numbers have a divisor in the first half
	for i in range(2, math.isqrt(num)):
		if num % i == 0:						# check if it is a prime number
			return False						# if not then terminate
	return True
	
def getPrime(size):
	while True:
		p = random.randrange(size, 2*size)		# get a prime number from the range size - 2x size
		if isPrime(p):
			return p

# check if g is a primitive root modulo p
# period of g**i must be (p - 1)
# period is the number of different results before they start repeating
def isGenerator(g, p):
	for i in range(1, p - 1):
		if (g**i) % p == 1:
			return False
	return True
			
# find a generator for the prime number p
def getGenerator(p):
	for g in range(2, p):
		if isGenerator(g, p):
			return g

print("1----------------------------------------------")
print("Diffie-Hellman key exchange")


print("\nPUBLIC")	
p = getPrime(1000)
g = getGenerator(p)
print("p = ", p)
print("g = ", g)


print("\nPRIVATE: Alice")
a = random.randrange(2, p)
print("a = ", a)
ga = (g**a) % p


print("\nPUBLIC")	
print("Alice sends the result of (g**a) % p to Bob publicly: ", ga)


print("\nPRIVATE: Bob")
b = random.randrange(2, p)
print("b = ", b)
gb = (g**b) % p


print("\nPUBLIC")
print("Bob sends the result of (g**b) % p to Alice publicly: ", gb)


print("\nPRIVATE: Alice")
commonA = (gb**a) % p
print("common secret: ", commonA)


print("\nPRIVATE: Bob")
commonB = (ga**b) % p
print("common secret: ", commonB)


# nowadays it is recommende to use eliptic curves instead of prime numbers!!!

"""
Diffie–Hellman key exchange establishes a shared secret between two parties 
that can be used for secret communication for exchanging data over a public network. 

An analogy illustrates the concept of public key exchange by 
using colors instead of very large numbers:

The process begins by having the two parties, Alice and Bob, 
publicly agree on an arbitrary starting color that does not need to be kept secret 
(but should be different every time[3]). In this example, the color is yellow. 
Each person also selects a secret color that they keep to themselves – in this case, red and cyan. 
The crucial part of the process is that Alice and Bob each mix their own secret color 
together with their mutually shared color, 
resulting in orange-tan and light-blue mixtures respectively, 
and then publicly exchange the two mixed colors. Finally,
each of them mixes the color they received from the partner with their own private color. 
The result is a final color mixture (yellow-brown in this case) that is identical 
to their partner's final color mixture.


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
