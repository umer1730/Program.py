def func():
    num = int(input("Enter num: "))
    if num%2==0:
        print("Num is even")
    else:
        print("odd")
func()

print()
print("---------2")
print()

score = int(input("Enter number: "))
if score <= 50:
    print("pass")
elif score >= 50:
    print("fail")

print()
print("---------2")
print()

age=int(input("Enter age: "))
if age >= 18:
    print("You are eligible to voot")
if age <= 18:
    print("You are not eligible to voot")

print()
print("---------2")
print()

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
op = input("Enter operator(+,-,*,/): ")
if op == '+':
    c= a+b
    print("Sum: ",c)
if op == '-':
    c= a-b
    print("minus: ",c)
if op == '*':
    c= a*b
    print("mul: ",c)
if op == '/':
    c= a/b
    print("div: ",c)

