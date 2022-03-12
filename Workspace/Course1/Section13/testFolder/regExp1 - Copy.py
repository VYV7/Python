print("========================================================================")

print("1--------------------------------")
text = "Is the phone here?"
print(text)

found = "phone" in text
print(found)


print("2--------------------------------")
import re					# improt regular expressions
# regular expressions (re) allow searching a text/file for a pattern 

pattern = "another pattern"
matchObj = re.search(pattern, text)
print(matchObj)

pattern = "phone"
matchObj = re.search(pattern, text)
print(matchObj)

matchIdx = matchObj.span()
print(matchIdx)
matchIdxStart = matchObj.start()
print(matchIdxStart)
matchIdxEnd = matchObj.end()
print(matchIdxEnd)


print("3--------------------------------")
# re returns only the first search result
text = "Is the first phone or the second phone here?"
print(text)

matchObj = re.search(pattern, text)
print(matchObj)


print("4--------------------------------")
# used the findall method to find all occurences of the pattern
matchObj = re.findall(pattern, text)
print(len(matchObj))
print(matchObj)

for matchObj in re.finditer(pattern, text):
	print(matchObj)






print("========================================================================")
