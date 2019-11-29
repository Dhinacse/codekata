n = int(input())
L = []
res = 'NO'
for i in range(n) :
    L2 = input().split()
    L.append(L2)
flag = False
for i in range(n-1) :
    for j in range(i+1,n) :
        if L[i][0] == L[j][1] and L[i][1] == L[j][0] :
            res = 'YES'
            break
print(res,end='')
