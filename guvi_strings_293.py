s=input().split()
i=1
l=[]
for j in s:
    if(i%2 != 0):
        l.append(j[::-1])
        i=i+1
    else:
        l.append(j)
        i=i+1
print(*l)
