

print("========================================================================")

print("1--------------------------------")
print("Circle")
class Sphere():
	pi = 3.14
	# attributes
	def __init__(self, radius):
		self.radius = radius
	# methods
	def surface_area(self):
		return 4 * Sphere.pi * self.radius**2
	def volume(self):
		return (4/3) * Sphere.pi * self.radius**3

s = Sphere(3)

print(s.surface_area())
print(s.volume())

print("2--------------------------------")
print("Guessing game")
import random
class GuessingGame():
	def __init__(self):
		self.rand_choice = random.randint(0,10)
		print(self.rand_choice)
		
	def reset_random(self):
		self.rand_choice = random.randint(0,10)
		print("Random number reset")
		print(self.rand_choice)
		
	def guess(self):
		num = int(input("Your guess: "))
		if num == self.rand_choice:
			print("Correct Guess")
			self.reset_random()
		elif num > self.rand_choice:
			print("Too high")
		elif num < self.rand_choice:
			print("Too low")

g = GuessingGame()
g.reset_random()
g.guess()


print("========================================================================")