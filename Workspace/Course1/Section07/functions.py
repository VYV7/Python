print("========================================================================")

def myfunction(argument):
	'''
	Docstring: This explains the function
	'''
	return "hello: "+argument
	
print(myfunction("Peter"))

print("1--------------------------------")

def reportAgent(name="Jason"):
	print("Reporting agent {}!".format(name))
	
reportAgent("Peter")
reportAgent()

print("2--------------------------------")

def secretCheck(string):
	return "secret" in string

print(secretCheck("Tadah!"))	
print(secretCheck("secret"))

print("3--------------------------------")
def codeMaker(string):
	'''
	INPUT: 	string
	OUTPUT: same string but with vowels replaced with x
	'''
	output = list(string)
	for index,letter in enumerate(string):
		for vowel in ["a","e","i","o","u"]:
			if letter.lower() == vowel:
				output[index] = "x"
			else:
				pass
							
	return "".join(output)

print(codeMaker("Hello"))







print("========================================================================")
