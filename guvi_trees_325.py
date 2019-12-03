n,k = map(int,input().split())
arr = list(map(int,input().split()))
while k>0:
    u,v = map(int,input().split())
    print(sum(arr[u-1:v]))
    k-=1 
