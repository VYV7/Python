print("========================================================================")
print("1--------------------------------")
try:
	1 + "1"
	#1 + int("a")
# if a type error occurs then print a message
except TypeError:
	print("You can only add integers")
# if a value error occurs then print a message
except ValueError:
	print("You can only add numbers")
# if no error
else:
	print("All good")

# type error
#1 + "1"
# value error
#print(int("a"))

print("2--------------------------------")
try:
	f = open("testfile","r")  # <--
	f.write("Example text")
#if an error
except:
	print("Error happend")
# if no error
else:
	print("All good")
# always runs
finally:
	print("This block of code always runs")

print("========================================================================")