L = input().split()
res = 'yes'
for x in L :
    if x[0].islower() :
        res='no'
    for i in range(1,len(x)) :
        if x[i].isupper():
            res = 'no'
print(res,end='')
