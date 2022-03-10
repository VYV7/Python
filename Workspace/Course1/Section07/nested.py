print("========================================================================")

print("3--------------------------------")
x = "outside"

def report():
	x = "inside"
	return x
	
print(x)
print(report())
print(x)

# The 4 scopes in order
#	Local
#	Enclosing
#	Global
#	Built-in



print("========================================================================")