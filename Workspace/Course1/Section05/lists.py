print("========================================================================")
mylist = []

s = "something"

print(mylist)
for letter in s:
	mylist.append(letter)
	print(letter)
print(mylist)


# list comprehension format
newlist = [letter for letter in s]
print(newlist)

squares = [x**2 for x in range(0,11)]
print(squares)

evens = [x for x in range(0,11) if x%2 == 0]
print(evens)

mylist = [x if x%2 == 0 else 'not even' for x in range(0,11)]
print(mylist)

print("========================================================================")