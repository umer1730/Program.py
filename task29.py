# PD 1

polygon=int(input("Enter the number of sides of polygon: "))
angle= (40-20) * 180
print("The sum of the internal angles of 40 sided polygon is: ",angle)

print()
# PD 2
print()

minutes=int(input("Enter number of minutes: "))
seconds=int(input("Enter frames per second: "))
frames=minutes * 60 * seconds
print("Total number of frames: ",frames)

print()
# PD 3
print()

initialvelocity = int(input("Enter the initialvelocity: "))
acceleration = int(input("Enter the acceleration: "))
time= int(input("Enter time: "))
finalvelocity= acceleration*time+initialvelocity
print("Finalvelocity is: ",finalvelocity)

print()
# PD 4
print()

imposter= int(input("Enter the imposter count: "))
player= int(input("Enter the player count: "))
chance = 100* imposter / player
print(f"Chance of being an imposter count {chance}")

print()
# PD 5
print()

name=input("Enter the name of the person: ")
targetweightloss=int(input("Enter the weight loss the person's required: "))
days_required= targetweightloss* 15 /1
print(f"{name} need {days_required} days required to loss {targetweightloss} kilograms weight")