print("========================================================================")

# range function
# generator. Does not store all elements in memory
for number in range(0,11,3):
	print(number)
	
#list = list(range(0,11,2))
print(list)

print("---------------------------------")
for letter in "abcde":
	print(letter)
	
print("")

index = 0
for letter in "abcde":
	print("At index {} the letter is {}".format(index,letter))
	index += 1

print("")

for count,letter in enumerate("abcde"):
	print("At index {} the letter is {}".format(count,letter))
	
print("")

# enumerate goes through a list and adds indexes to its elements.
# it stores the result as a list of tuples
list1 = tuple(enumerate('word'))
print(list1)
print(list1[3][1])

print("---------------------------------")

# joining two lists into a tuple
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

for mytuple in zip(mylist1,mylist2):
	print(mytuple)
	
list = list(zip(mylist1,mylist2))
print(list)

print("---------------------------------")

# cheking if a list contains an item
boolvar = "x" in ["a", "b", "c"]
print(boolvar)

boolvar = "x" in "Tedx"
print(boolvar)

print("---------------------------------")

mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

print("---------------------------------")

#shuffle
from random import shuffle
print(mylist)
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

print("---------------------------------")

#random integer generator
from random import randint
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))
	
print("========================================================================")