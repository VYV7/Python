print("========================================================================")

print("1--------------------------------")
# map function (map(<func>,<sequence>)
# iterates through the sequence and returnes 
# what func returnes after calling it
# with items from the sequence
def square(num):
	return num**2

mynums = [1,2,3,4,5]

print(list(map(square, mynums)))


print("2--------------------------------")
# filter function (filter(<func>,<sequence>)
# iterates through the sequence and returnes 
# items for which the func returned True
def check_even(num):
	return num%2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums)))


print("3--------------------------------")
# lambda function (map(<func>,<sequence>)

# normal function definition
#def square(num):
#	return num**2

# compressed function definition
def square(num): return num**2

# lambda expression (anonnymous because hasn't got any name)
lambda num: num**2

mynums = [1,2,3,4,5]

print(list(map(square, mynums)))
print(list(map(lambda num: num**2, mynums)))


print("4--------------------------------")

print(list(filter(lambda n:n%2==0, mynums)))

string = ["Example", "Another", "coffee"]

print("".join(map(lambda s:s[0], string)))






print("========================================================================")