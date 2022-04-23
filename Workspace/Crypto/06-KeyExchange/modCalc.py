# clock 0 to 11
# generators
print("=============================================================")
print("Generators\n")

val = (4 + 7) % 12
print("(4 + 7) % 12 = ", val)

val = (4 * 7) % 12
print("(4 * 7) % 12 = ", val)

print("\nGenerator")

g = 2
for i in range(20):
	result = (g**i) % 11
	print("g**",i, " % 11 = ", result)
	



print("=============================================================")
