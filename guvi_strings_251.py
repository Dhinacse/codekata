from itertools import permutations
s = input()
L = list(permutations(s,len(s)))
L2 = [ ''.join(x)  for x in L]
print(*L2,sep='\n')
