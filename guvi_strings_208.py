from collections import OrderedDict
def dup(str): 
    return "".join(OrderedDict.fromkeys(str))
if __name__ == "__main__": 
    str = input()
    print (dup(str))
