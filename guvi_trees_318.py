n = int(input())
arr = list(map(int,input().split()))
s = set(arr)
d = {}
for x in s:
    d[arr.count(x)] = x
print(d[max(d.keys())])
