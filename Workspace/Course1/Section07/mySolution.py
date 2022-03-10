print("========================================================================")

print("\nTask 1 -------------------------------------------")
print("Create a function that takes in two integers and \n\
	returns True if their sum is 10, False otherwise.\n")

def check_ten(n1,n2):
	if n1 + n2 == 10:
		return True
	else:
		return False
	
print(check_ten(10,0))
print(check_ten(10,2))

print("\nTask 2 -------------------------------------------")
print("Create a function that takes in two integers and\n\
	returns True if their sum is 10, otherwise,\n\
	return the actual sum value")
	
def check_ten_sum(n1,n2):
	if n1 + n2 == 10:
		return True
	else:
		return n1+n2
	
print(check_ten_sum(10,0))
print(check_ten_sum(10,2))

print("\nTask 3 -------------------------------------------")
print("Create a function that takes in a string and\n\
	returns back the first character of that string in\n\
	upper case.")
	
def first_upper(mystring):
	return mystring.upper()[0]
	
print(first_upper("my name"))

print("\nTask 4 -------------------------------------------")
print("Create a function that takes in a string and \n\
	returns the last two characters. If there are \n\
	less than two chracters, return the string: 'Error'")
	
def last_two(mystring):
	if len(mystring) > 1:
		lastTwo = []
		lastTwo.append(mystring[-2])
		lastTwo.append(mystring[-1])
		return "".join(lastTwo)
	else:
		return "Error"
	
print(last_two("Example"))

print("\nTask 5 -------------------------------------------")
print("Given a list of integers, return True if \n\
	the sequence [1,2,3] is somewhere in the list.\n\
	Hint: Use slicing and a for loop.")
	
def seq_check(nums):
	for idx in range(len(nums)-2):
		if nums[idx]==1 and nums[idx+1]==2 and nums[idx+2]==3:
			return True
	return False
	
print(seq_check([0,1,2,3,4,5]))
print(seq_check([0,1,3,4,5]))

print("\nTask 6 -------------------------------------------")
print("Given a 2 strings, create a function that\n\
	returns the difference in length between them.\n\
	This difference in length should always be\n\
	a positive number (or just 0). Hint: Absolute Value")
	
def compare_len(s1,s2):
	return abs(len(s1) - len(s2))
	
print(compare_len("test","longer"))
print(compare_len("test","test"))
print(compare_len("Warrior","Me"))

print("\nTask 7 -------------------------------------------")
print("Given a list of integers, if the length of the list\n\
	is an even number, return the sum of the list.\n\
	If the length of the list is odd, return the max value.")
	
def sum_or_max(mylist):
	sum = 0
	if len(mylist) % 2 == 0:
		for num in mylist:
			sum = sum + num
		return sum
	else:
		return max(mylist)

print(sum_or_max([1,2,3,4]))
print(sum_or_max([1,2,3,4,5]))

print("\nTask 8 -------------------------------------------")
print("Agents in the field sometimes need to speak in code.\n\
	Create a function that replaces all vowels\n\
	with the letter x.\n\
	Then switch the position of the first and last letters")
	
def replace_and_switch(name):
	namelist = list(name)
	for index,letter in enumerate(namelist):
		for vawel in ['a','e','i','o','u']:
			if letter.lower() == vawel:
				namelist[index] = "x"
				
	last = namelist[-1]
	namelist[-1] = namelist[0]
	namelist[0] = last
	
	return "".join(namelist)
	
print(replace_and_switch("Alfred"))









print("========================================================================")