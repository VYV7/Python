print("###############################################################################")
import cProfile		# the run method gathers profiling stats from the execution

# function implementing factorial
def factorial(n):
	if n == 1:
		return n
	else:
		return factorial(n-1)*n
		
def counter(n):
	cnt = 0
	for i in range(n):
		cnt += 1
	return cnt
	
###############################################################################
print("1--------------------------------")
cProfile.run("counter(factorial(10))")


print("\n2--------------------------------")
cProfile.run("counter(factorial(11))")







print("###############################################################################")