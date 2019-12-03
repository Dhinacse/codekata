def xor(arr,u,v):
    k = arr[u-1]
    for i in range(u,v):
        k = k^arr[i]
    return k 

n,k = map(int,input().split())
arr = list(map(int,input().split()))
while k>0:
    u,v = map(int,input().split())
    print(xor(arr,u,v))
    k-=1  
