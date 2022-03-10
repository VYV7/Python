print("========================================================================")

mystring = "Secret agents are super good at staying hidden."
print(mystring)

print("\nTask 1 -------------------------------------------")
print("Words starting with s")
for word in mystring.split():
    if word[0] == 'S' or word[0] == 's':
        print(word)
		
print("\nTask 2 -------------------------------------------")
print("Words with even number of letters")
for word in mystring.split():
    if len(word)%2 == 0:
        print(word)
		
print("\nTask 3 -------------------------------------------")
print("List comprehension to create a list of first letters")
print([word[0] for word in mystring.split()])

print("\nTask 4 -------------------------------------------")
print("List comprehension to create a list of even numbers from 0 to 10")
print([num for num in range(0,11) if num%2 == 0])

print("\nTask 5 -------------------------------------------")
print("Use the range function to create a list of all even numbers from 0 to 100")
print( list(range(0,11,2)) )

print("\nTask 6 -------------------------------------------")
print("Create a for loop that uses the random lib to create a list of 10 random numbers")
from random import randint
randlist = []
for i in range(0,10):
	randlist.append(randint(0,100))
print(list(randlist))	

print("\nTask 7 -------------------------------------------")
print("Use list comprehension and the random library to create a list of 10 random numbers")
print([randint(0, 101) for randnum in range(0,10)])

print("\nTask 8 -------------------------------------------")
print("Use list comprehension and the random library to create a list of 10 random numbers")
userinput = 1
while userinput%2 != 0:
	userinput = int(input("Enter an even number: "))

	if userinput%2 == 0:
		print("This is an even number")
		
print("========================================================================")

