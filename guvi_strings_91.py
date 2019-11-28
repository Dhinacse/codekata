s=input()
x=0
for i in s:
    if(i=='('):
        x=x+1
    elif(i==')'):
        x=x-1
if(x==0):
    print("yes")
else:
    print("no")
