print("========================================================================")

mylist = [1,2,3,4,5]
print(mylist)

mylist.append(2)
print(mylist)

print(mylist.count(2))
print(type(mylist))

print("1--------------------------------")
class Sample():
	pass
	
x = Sample
	
print(type(Sample))
print(type(x))

print("1--------------------------------")

class Agent():
	# class object attribute
	# it will be set for every instance of the object
	planet = "Earth"
	
	# special class to initialise ATTRIBUTES of the object
	# based on parameters passed when creating an instance of
	# the object 
	def __init__(self,name, eye_color):
		self.real_name = name				# attribute 1
		self.eye_color = eye_color			# attribute 2

x = Agent("Peter", "Blue")
print(type(x))
print(x.real_name)
print(x.eye_color)





print("========================================================================")