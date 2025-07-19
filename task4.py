time = int(input("Enter time (0-23):"))
if time >= 6 and time < 12:
    print("Good morning")
elif time >= 12 and time < 18:
    print("Good afternoon")
elif time >= 18 and time <= 23 or time >= 0 and time < 6:
    print("Good evening")
else:
    print("Invalid time entered")

 # next code  
playerhealth = 1000 - 100
print(playerhealth)
# next code
num_bananas = 10
f_string = f"You have {num_bananas} bananas"
print(f_string)
# You have 10 bananas