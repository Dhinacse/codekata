input = int(input())
output = [] 
y=0
while input>0: 
	rem = input % 10
	input = int(input / 10)
	y=y+rem**2
	output.append(rem) 
print(y) 
