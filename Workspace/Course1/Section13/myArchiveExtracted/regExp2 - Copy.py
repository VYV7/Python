print("========================================================================")
import re		# regular expressions

print("1--------------------------------")
# character identifiers
# \d 	a digit				file_\d\d		file_25
# \w	alphanumeric		\w-\w\w\w		A-b_1
# \s 	white space			a\sb\sc			a b c
# \D	non digit			\D\D\D			ABC
# \W	non-alphanimeric	\W\W\W\W\W		*-+=)
# \S	non-whitespace		\S\S\S\S		Yoyo

text = "My phone number is 408-555-1234"

# when we know what we're looking for
matchObj = re.search("408-555-1234", text)
print(matchObj)

# when we only know the pattern of what we're looking for
# ddd-ddd-dddd
matchObj = re.search("\d\d\d-\d\d\d-\d\d\d\d", text)
print(matchObj)

text = "My phone number is 408-567-1234"
matchObj = re.search("\d\d\d-\d\d\d-\d\d\d\d", text)
print(matchObj)


print("2--------------------------------")
# quantifiers -specify how many timers a char is repeated in the pattern
# +		occurs one or more times		Version \w-\w+		Version A-b1_1
# {3}	occurs exactly 3 times			\D{3}				abc
# {2,4}	occurs 2 to 4 times				\d{2,4}				123
# {3,}	occurs 3 or more times			\w{3,}				anycharacters
# *		occurs 0 or more times			ABC*				AAACC
# ?		once or none					plurals?			plural

matchObj = re.search("\d{3}-\d{3}-\d{4}", text)
print(matchObj)


print("3--------------------------------")
# use the compile method to make a pattern that 
# consists of multiple groups
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(1))



print("========================================================================")
