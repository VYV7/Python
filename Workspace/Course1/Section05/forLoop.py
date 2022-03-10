print("========================================================================")

mylist = [0,1,2,3,4]
for variable in mylist:
	print(variable)
print("------------------------------------")

myword = "Hello"
for letter in myword:
	print(letter)
print("------------------------------------")

mytuplelist = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for (n1,n2) in mytuplelist:
	print (n1,n2)
print("------------------------------------")

mydict = {"a":1, "b":2, "c":3}
for dict in mydict:
	print(dict)

for dict in mydict.items():
	print(dict)
	
for (key,value) in mydict.items():
	print(key, value)
	
for key in mydict:
	print(mydict[key])
print("------------------------------------")

for letter in "code":
	if letter == 'd':
		continue
	print(letter)
	
print("========================================================================")