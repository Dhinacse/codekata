n = int(input())
arr = list(map(int,input().split()))
k = arr[0]
for i in range(1,len(arr)):
    k = k|arr[i]
print(k)
