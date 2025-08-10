voltage=float(input("Enter voltage: "))
current=float(input("Enter current: "))
power=voltage / current
print(f"The power is: {power}")

print()
print("-------------")
print()

age=int(input("Enter your age: "))
days=age * 365
print(f"Total days in {age} years is: {days}")

print()
print("-------------")
print()

from colorama import Fore,Style,init
population=int(input("Enter population: "))
rate=int(input("Enter rate: "))
decades= population / 30
print(Fore.BLUE+f"The population of three decades is: {decades}")

print()
print("-------------")
print()

wins=int(input("Enter the number of wins: "))
draws=int(input("Enter the number of draws: "))
losses=int(input("Enter the number of losses: "))
points = 1 * 3
print(Fore.GREEN+"Points is: ",points)

print()
print("-------------")
print()

megabytes=float(input("Enter megabytes: "))
kilobytes=float(input("Enter kilobytes: "))
bits= megabytes * 1024*1024*8
print(f"{megabytes} megabytes is equivalent to {bits} bits")

print()
print("-------------")
print()

hours=int(input("Enter hours: "))
seconds=hours * 3600
print(f"Hours is equal to {seconds} seconds")

print()
print("-------------")
print()

age=int(input("Enter person's age: "))
if (age > 18):
    print("person1")
else:
    print("person2")

print()
print("-------------")
print()