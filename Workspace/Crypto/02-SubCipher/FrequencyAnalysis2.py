print("###############################################################################")
import operator
import sys

cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""
			  
#------------------------------------------------------------------------------			  
class Attack:
	def __init__(self):
		self.alphabet = "abcdefghijklmnopqrstuvwxyz"
		self.plainCharLeft = "abcdefghijklmnopqrstuvwxyz"
		self.cipherCharLeft = "abcdefghijklmnopqrstuvwxyz"
		self.freq = {}
		self.mapping = {}
		self.key = {}
		self.freq_eng = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
						'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
						'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
						's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
						'y': 0.0197, 'z': 0.0007}
						
	#--------------------------------------------	
	def calculate_freq(self, cipher):
		# reset freq counter for each letter
		for letter in self.alphabet:
			self.freq[letter] = 0	
		
		letter_cnt = 0									# total number of letters in the cipher
		
		# count the total number of letters and how many times they occured
		for letter in cipher:
			if letter in self.freq:
				self.freq[letter] += 1
				letter_cnt += 1

		# calculate the letter occurence to text length ratios		
		for letter in self.freq:
			self.freq[letter] = round( (self.freq[letter] / letter_cnt), 4)
			
	#--------------------------------------------		
	def print_freq(self):
		# print the result
		for letter in self.freq:
			print(letter, ":", self.freq[letter])
			
	#--------------------------------------------		
	def calc_matches(self):
		map = {}
		for cipherChar in self.alphabet:
			for plainChar in self.alphabet:
				map[plainChar] = round( abs( self.freq[cipherChar] - self.freq_eng[plainChar] ), 4 )
	
			#print(cipherChar, " map{}: ", map)
			self.mapping[cipherChar] = sorted( map.items(), key=operator.itemgetter(1) )
		#DEBUG
		#for i in self.mapping:
			#print("self.mapping:\n", i, " ", self.mapping[i])
			
	#--------------------------------------------		
	def set_key_mapping(self, cletter, letter):	
		if cletter not in self.cipherCharLeft or letter not in self.plainCharLeft:
			print("ERROR: key mapping error", cletter, letter)
			sys.exit(-1)
			
		self.key[cletter] = letter
		self.plainCharLeft = self.plainCharLeft.replace(letter, "")
		self.cipherCharLeft = self.cipherCharLeft.replace(cletter, "")
	
			
	#--------------------------------------------		
	def guess_key(self):		
		# go through all letters in the alphabet
		for letter in self.cipherCharLeft:
		
			# for each letter go through their list of characters and differences
			for cletter, diff in self.mapping[letter]:		
				#print("cletter: ", cletter, " ", diff)
			
				# if that letter is in the remaining letters of the alphabet
				# then add it to the key dictionary and remove it from 
				# the available letters to avoid duplication
				if cletter in self.plainCharLeft:
					self.key[letter] = cletter
					self.plainCharLeft = self.plainCharLeft.replace(cletter, "")
					break
	
	#--------------------------------------------		
	def get_key(self):
		return self.key
	
	
	
#------------------------------------------------------------------------------			
		
def decrypt(key, cipher):
	message = ""
	for letter in cipher:
		if letter in key:
			message += key[letter]
		else:
			message += letter
	return message
	
	

###############################################################################
# we know it is english
# we know average frequency of letter

attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()		
attack.calc_matches()

# based on the result above we can conclude other letters
attack.set_key_mapping("p", "h")
attack.set_key_mapping("r", "e")
attack.set_key_mapping("m", "a")
attack.set_key_mapping("v", "c")
attack.set_key_mapping("w", "i")
attack.set_key_mapping("t", "y")
attack.set_key_mapping("q", "k")
attack.set_key_mapping("o", "g")
attack.set_key_mapping("y", "m")
attack.set_key_mapping("e", "v")
attack.set_key_mapping("d", "d")
attack.set_key_mapping("x", "f")
attack.set_key_mapping("u", "r")
attack.set_key_mapping("s", "p")
attack.set_key_mapping("a", "x")


attack.guess_key()
key = attack.get_key()

message = decrypt(key, cipher)
messageLines = message.splitlines()

cipherLines = cipher.splitlines()

print("\nKey: ", key)


for line in range(0, len(messageLines)):
	print("P: ", messageLines[line])
	print("C: ", cipherLines[line])

		
		
		
		
		
		
		
		
		
		
		
		
		
		
print("###############################################################################")
