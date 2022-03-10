print("========================================================================")

print("1--------------------------------")

# define Circle
class Circle():
	pi = 3.14
	
	# attributr initialisation
	def __init__(self,radius=1):
		self.radius = radius
	
	# methods
	def area(self):
		return self.radius * self.radius * Circle.pi
	def perimeter(self):
		return self.radius * Circle.pi * 2
	def report(self,name):
		return "Report {}".format(name)
	
	
# create instances of Circle	
c1 = Circle(5)
c2 = Circle()

print(c1.radius)
print(c1.area())
print(c1.perimeter())
print(c1.report("John"))
print("\n")
print(c2.radius)
print(c2.area())
print(c2.perimeter())
print(c2.report("Sally"))

print("2--------------------------------")
# inheritance

class Person():
	# attribut initialisation
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
	# methods
	def report(self):
		print("I am {} {}".format(self.firstName, self.lastName))
	def hello(self):
		print("Hello!")
			
p1 = Person("James", "Bond")
p1.report()

# Agent inherits Person
class Agent(Person):
	# attribute initialisation
	def __init__(self, firstName, lastName, codeName):
		Person.__init__(self, firstName, lastName)
		self.codeName = codeName
		
	# overwriting Person's method
	def report(self):
		print("Hello, I'm {}".format(self.codeName))
	# new methods
	def realName(self, passcode=0):
		if passcode==123:
			print("My real name is {} {}".format(self.firstName,self.lastName))
		else:
			print("I can't tell you")
		
a1 = Agent(firstName="James",lastName="Bond",codeName="007")
print(a1.firstName)
a1.report()
a1.realName()
a1.realName(123)









print("========================================================================")