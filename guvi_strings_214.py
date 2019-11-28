user_input = input()
try:
    hexval = int(user_input, 16)
    print ("yes")
except:
    print ("no")
