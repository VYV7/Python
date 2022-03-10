print("========================================================================")
# Imports you might need
import string
import random


class Encryption():

	def __init__(self,seed):

		# Set a random seed and a self.seed attribute
		random.seed(seed)
		self.seed = seed

		# Create an empty string attribute to hold the encrypted phrase
		self.encrypted = ""

		# Use the string and random libraries to create two attributes
		# One is the correct alphabet, another is a shuffled alphabet (hint: random.sample())
		self.alphabet = list(string.ascii_lowercase)
		self.alphabet_sh = random.sample(self.alphabet, len(self.alphabet))

	def encryption(self,message):
		'''
		This method will take in a string message and encrypt it. Check the video or 
		the instructions above in the markdown for full description of how your
		decryption method should work.

		'''
		stuffed = ""
		################################################################
		### STEP 1: ADD A RANDOM LETTER IN EVERY SECOND POSITION    ###
		##############################################################
		for i in range(len(message)):
			stuffed += message[i]									# original letter
			stuffed += random.sample(self.alphabet, 1)[0]			# then random letter
			
		#################################################
		### STEP 2: REVERSE THE STRING  ################
		###############################################
		self.encrypted = stuffed[::-1]								# reverse order

		##########################################################################
		##### STEP 3: USE THE RANDOM SHUFFLED ALPHABET FOR A CEASER CIPHER ######
		########################################################################
		encrypted2 = list(range(len(self.encrypted)))				# generate a list of numbers
		
		for i,letter in enumerate(self.encrypted.lower()):			# go through all letters in encrypted msg
		
			if letter in self.alphabet:								# if it is a letter in alphabet
				index = self.alphabet.index(letter)					# get its index in the alphabet
				encrypted2[i] = self.alphabet_sh[index]				# get a letter from the shuffled set
			else:
				# Punctuation and spaces
				encrypted2[i] = letter								# else keep spaces and punctuation

				
		self.encrypted = "".join(encrypted2)
		return self.encrypted
		

	def decryption(self,message,seed):
		'''
		This method takes in a messsage and a seed for the random shuffled alphabet.
		It then returns the decrypted alphabet.
		'''
		decrypted = list(range(len(message)))					# create a list
		
		# Set a random seed and a self.seed attribute
		random.seed(seed)
		self.alphabet_sh = random.sample(self.alphabet, len(self.alphabet))
		
		for i,letter in enumerate(message.lower()):
			if letter in self.alphabet:
				index = self.alphabet_sh.index(letter)
				decrypted[i] = self.alphabet[index]
			else:
				decrypted[i] = letter
		
			
		decrypted = "".join(decrypted)[::-1]	
		return decrypted[::2]

e = Encryption(20)
enc = e.encryption("hello world")
print(enc)
dec = e.decryption(enc, 20)
print(dec)





















print("========================================================================")