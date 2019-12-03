n = int(input()) 
a = list(map(int,input().strip().split()))[:n] 
y=a[::-1]
print( ' '.join(map(str, y)))
