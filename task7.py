names=["milo","sara","bruno","bravo","dols","ffaf"]
namesWith_0=[item for item in names if "o" in item]
print(namesWith_0)
# AND
def cal(a,b):
    sum = a + b
    print(sum)
    
cal(a=1,b=2)
# and
def printDiamond(n):
    for i in range(n):
        print(" " * (n-i-1)+"*"*(2*i+1))
    for i in range(n-2,-1,-1):
        print(" "*(n-i-1)+"*"*(2*i+1))
printDiamond(5)

