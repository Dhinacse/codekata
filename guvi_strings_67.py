s = input()
y=''.join([ s[x:x+2][::-1] 
for x in range(0, len(s), 2) ])
print(y)
