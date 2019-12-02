n = int(input())
L = [int(x) for x in input().split()]
for x in set(L) :
    if L.count(x)==1 :
        res = x
        break
print(res,end='')
