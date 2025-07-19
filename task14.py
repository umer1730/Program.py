choices = ["snake", "water", "gun"]
user = input("Choose snake, water, or gun: ")
computer = input("Choose snake,water,gun:")

print(f"You choose: {user}")
print(f"Computer choose: {computer}")
if user == computer:
    print("It's a tie!")
elif (user == "snake" and computer == "water") or \
     (user == "water" and computer == "gun") or \
     (user == "gun" and computer == "snake"):
    print("You win!")
else:
    print("Computer wins!")