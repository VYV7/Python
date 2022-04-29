print("=============================================================")
"""
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

RSA - (Rivest-Shamir-Adleman) public key cryptosystem
publicaly described in 1977
equvalent system was developed by GCHQ in 1973 (made public in 1997)
- 	asymetric encryption: encryption key is public, decryption key is secret.
- 	user creates and publishes the public key based on two large prime numbers
	and an auxiliary value.
-	prime numbers are kept secret
-	messages can be encrypted by anyone and decrypted by the person
	who knows the prime numbers.
"""
#==============================================================================	
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
	
# calculates lcm(a, b) with the following formula
# lcm(a,b) = |ab| / gcd(a-1, b-1)	
def lcm(a, b):
	return a*b // math.gcd(a, b)
	
# generate exponent e
# 1 < e < lembda_n, gcd(e, lambda_n) = 1
def getE(lambda_n):
	for e in range(2, lambda_n):
		if math.gcd(e, lambda_n) == 1:
			return e
	return False

# solve the equation de = 1 (mod lambda_n) for d
def getD(e, lambda_n):
	for d in range(2, lambda_n):
		if d*e % lambda_n == 1:
			return d
	return False
	
#==============================================================================					
print("Key generation")
print("\nStep 1:")
print("generate 2 distinct prime numbers - p and q")
print("p and q are secret!")
size = 300
p = getPrime(size)
q = getPrime(size)
print("\tp: ", p)
print("\tq: ", q)


print("\nStep 2:")
print("calculate n = p * q")
n = p * q
print("\tn = p * q = ", n)

print("\nStep 3:")
print("calculate lambda(n) = lcm(p-1, q-1)")
print("lambda is Carmichael's totient function")
print("since n = pq, lambda(n) = lcm(lambda(p), lambda(q))")
print("and since p and q are prime, lambda(p) = phy(p) = p - 1")
print("and the same for q")
print("the lcm may be calculated through Euclidean algorithm")
print("lcm(p,q) = |ab| / gcd(p,q)")
lambda_n = lcm(p-1, q-1)
print("\tlambda_n = lcm(p-1, q-1) = ", lambda_n)

print("\nStep 4:")
print("generate public exponent e [1 < e < lembda_n, gcd(e, lambda_n) = 1]")
e = getE(lambda_n)
print("\te = ", e)

print("\nStep 5:")
print("solve the equation de = 1 (mod lambda_n) for secret exponent d")
print("d is secret!")
d = getD(e, lambda_n)
print("\td = ", d)


print("----------------------------------")
print("SUMMARY:")
print("Generated primes: ", p, q)
print("Modulus n: ", n)
print("Lambda n: ", lambda_n)
print("Public exponent: ", e)
print("Secret exponent: ", d)
print("Public key (e, n):", e, n)
print("Secret key (d):", d)


print("----------------------------------")
print("Bob")
m = 117
print("message: ", m)
c = m**e % n			# create cipher
print("cipher: ", c)

print("\nAlice")
mDec = c**d % n
print("Decrypted cipher: ", mDec)


print("=============================================================")
