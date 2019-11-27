n=input()
y=input()
l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if(sorted(l)==sorted(n+y)):
    print("complementary")
else:
    print("non-complementary")
