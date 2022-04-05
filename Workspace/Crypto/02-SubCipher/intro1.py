# permutations
# N! = N*(N-1) * N*(N-2) * ... * N*1
# example 16 = 4 * 3 * 2 * 1

from itertools import permutations

myList = [1,2,3,4,5]

permList = permutations(myList)
cnt = 0

for perm in permList:
	#print(perm)
	cnt += 1
	
print("Nunber of permutations: ", cnt)