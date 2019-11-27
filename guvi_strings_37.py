a,K=input().split()
s=len(a)
for x in a:
    if(x == K):
        e=(a.index(x))
        s=e+1
        print(s)
