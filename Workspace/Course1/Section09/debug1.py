print("========================================================================")

print("1--------------------------------")
# import python debugger
import pdb

x = "1"
y = 2
z = 3

result = y + z
print(result)

pdb.set_trace() # q Enter to exit

newResult = y + x
print(newResult)



print("========================================================================")