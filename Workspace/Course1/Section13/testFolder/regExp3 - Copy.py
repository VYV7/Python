print("========================================================================")
import re		# regular expressions

print("1--------------------------------")
# Or operator
matchObj = re.search("cat", "The cat is here")
print(matchObj)

matchObj = re.search("cat", "The dog is here")
print(matchObj)

matchObj = re.search("cat|dog", "The dog is here")
print(matchObj)


print("2--------------------------------")
# wildcart operator (.) stands for all chars
matchObj = re.findall("at", "The cat in the hat sat there")
print(matchObj)
matchObj = re.findall("...at", "The cat in the hat sat there")
print(matchObj)
matchObj = re.findall(".at", "The cat in the hat sat there")
print(matchObj)


print("3--------------------------------")
# checking if a string starts with (^) a specific character
matchObj = re.findall("^\d", "3 is the number")
print(matchObj)
matchObj = re.findall("^\d", "The 3 is the number")
print(matchObj)

# checking if a string ends with ($) a specific character
matchObj = re.findall("\d$", "The number is 2")
print(matchObj)
matchObj = re.findall("\d$", "The number is two")
print(matchObj)


print("4--------------------------------")
# exclusion [] - good for removing punctuation from sentences

phrase = "There are 3 numbers 34 inside 5 this sentence"
print(phrase)

pattern = "[^\d]"		# exclude all digits
matchObj = re.findall(pattern, phrase)
print(matchObj)

pattern = "[^\d]+"		# exclude all digits, (+) put words together
matchObj = re.findall(pattern, phrase)
print(matchObj)

pattern = "[^\d ]+"		# exclude all digits, (+) put words together
matchObj = re.findall(pattern, phrase)
print(matchObj)

pattern = "[^\d ]+"		# exclude all digits, (+) put words together
matchObj = re.findall(pattern, phrase)
print(" ".join(matchObj))


print("5--------------------------------")
# exclusion []

phrase = "Only find hypen-words in this text. Semi-colon"
print(phrase)

pattern = "[\w]+"	# find only words
matchObj = re.findall(pattern, phrase)
print(matchObj)

pattern = "[\w]+-[\w]+"	# hipenated words 
matchObj = re.findall(pattern, phrase)
print(matchObj)



print("========================================================================")
