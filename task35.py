n = int(input("Enter num: "))
while(n < 10):
    if n == 5:
        n = n +1
        continue
    print(f"n = {n}")
    n = n+1

print()
print("---------2")
print()

number = 6
while (number > 0):
    print(number , " ")
    number -= 2

print()
print("---------2")
print()

# username=input("Enter name: ")
# while True:
#     print(username)
    
#     print()
#     print("---------2")
#     print()

#     name = input("Your name: ")
#     while True:
#         print("Your name: ",name)

print()
print("---------2")
print()

distance = float(input("ENter distance: "))
fuel = distance * 10
if fuel < 100:
    print("fuel is more  than 100")
else:
    print("Fuel is less then 100")    

print()
print("---------2")
print()

day = input("Enter day of the purchase: ")
a = input("Enter day of total purchase amount: $")
if day == "Sunday":
    b = a-(a*0.10)
    print("Payable amount: $",b)
elif day == "Monday":
    b = a
    print("Payable amount : $",b)
else:
    print("Invalid day")