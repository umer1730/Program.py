for i in range(6):
    print(i)
    if i == 4:
       break
else:
    print("sorry no i")
#next code
for i in range(6):
    print("iteration no {} in for loop".format(i+1))
else:
    print("else block in loop")
print("out of loop")
#next code
#table
a =input("Enter number:")
print(f"Multiplication table of {a} is")
for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
    #next code
    #exception handling in python
a =input("Enter number:")
print(f"Multiplication table of {a} is")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:                                         #except as exception in e:
    print("Invalid error!")   
print("Some handling.........")
print("End of program")      