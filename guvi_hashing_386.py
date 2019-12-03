i = 1
k = 1
j = 97
d = {}
for m in range(26):
	le = chr(j)
	d[le] = i*k
	k*=-1
	j+=1
	i+=1
#print(d)
t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    for x in s.lower():
    	sum+=d[x]
    print(sum)
