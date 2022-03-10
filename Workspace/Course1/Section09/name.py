print("========================================================================")
# In larger scripts at the bottom you will find
# if __name__ == "__main__"
# this line of code is designed to indicate where cunction calls are 
# coming from when working with multiple files.

import mymodule

print("Top level in name.py")
mymodule.my_func()

# if the script is run directly
if __name__=="__main__":
	print("name.py is being run directly")
# if the script is run from another module
else:
	print("name.py is being imported into another module")

print("========================================================================")