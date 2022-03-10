import string
print("========================================================================")
def encrypt(text,shift):
	'''
	INPUT: text as a string and an integer for the shift value.
	OUTPUT: The shifted text after being run through the Caeser cipher.
	'''
	# Create a normal plain alphabet OK
	encrypted_text = list(range(len(text)))
	alphabet = string.ascii_lowercase
	# Create a shifted version of this alphabet 
	# (Try slicing using the shift and then reconcatenating the two parts)
	part1 = alphabet[:shift]
	part2 = alphabet[shift:]
	shifted = part2 + part1
	# Use a for loop to go through each character in the original message.
	# Then figure out its index match in the shifted alphabet and replace.
	# It might be helpful to create an output variable to hold the new message.	
	# Keep in mind you may want to skip punctuation with an if statement.
	for i,letter in enumerate(text.lower()):
		if letter in alphabet:
		
			original_index = alphabet.index(letter)
			new_letter = shifted[original_index]
			encrypted_text[i] = new_letter
			
		else:
			encrypted_text[i] = letter	
	# Return the shifted message. Use ''.join() method 
	# if you still have it as a list.  
	return "".join(encrypted_text)
	
def decrypt(text,shift):
	'''
	INPUT: text as a string and an integer for the shift value.
	OUTPUT: The shifted text after being run through the Caeser cipher.
	'''
	# Create a normal plain alphabet
	decrypted_text = list(range(len(text)))
	alphabet = string.ascii_lowercase
	# Create a shifted version of this alphabet 
	# (Try slicing using the shift and then reconcatenating the two parts)
	part1 = alphabet[:shift]
	part2 = alphabet[shift:]
	shifted = part2 + part1
	# Use a for loop to go through each character in the original message.
	# Then figure out its index match in the shifted alphabet and replace.
	# It might be helpful to create an output variable to hold the new message.	
	# Keep in mind you may want to skip punctuation with an if statement.
	for i,letter in enumerate(text.lower()):
		if letter in alphabet:
		
			index = shifted.index(letter)
			original_letter = alphabet[index]
			decrypted_text[i] = original_letter
			
		else:
			decrypted_text[i] = letter	
	# Return the shifted message. Use ''.join() method 
	# if you still have it as a list.  
	return "".join(decrypted_text)

def brut_force(message):
	for n in range(26):
		print("Using a shift value of {}".format(n))
		print(decrypt(message,n))
		print("\n")

text = 'get this message to the main server'	
encrypted = encrypt(text, 13)
decrypted = decrypt(encrypted, 13)
print("Original message: {}".format(text))
print("Encrypted message: {}".format(encrypted))
print("Decrypted message: {}".format(decrypted))

brut_force(encrypted)














print("========================================================================")