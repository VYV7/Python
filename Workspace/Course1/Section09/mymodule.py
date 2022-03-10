def my_func():
	print("This is my function from mymodule.py")
	
def my_func1():
	print("This is my function 1 from mymodule.py")
	
def my_func2():
	print("This is my function 2 from mymodule.py")
	
	
print("Top level in mymodule.py")

if __name__ == "__main__":
	print("mymodule.py is being run directly")
else:
	print("mymodule.py is being run in another module")