n = int(input())
l = []
for i in range(n,0,-1):
    l.append([1]*i)
for x in l:
    print(*x)
