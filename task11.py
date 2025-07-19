x = input("Enter word:")
y = int(input("enter no:"))
print(f"{x} get the first position by {y} points ")

#next code
a = "hello"
reversed_a = a[::-1]
print("a:",reversed_a)
#next
x = "harry"
print(x.center())
#NEXT CODE
def myfunc(n):
    return lambda x : x * n
tripler = myfunc(3)
print(tripler(11))
