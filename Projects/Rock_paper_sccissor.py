import random
item_list = ["Rock","Paper","Scissor"]
user_choice = input("Enter user choice(Rock,Paper,Scissor = ")
comp_choice = random.choice(item_list)
print(f"User choice = {user_choice},\nComputer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same = match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper  cover the Rock = Computer win")
    else:
        print("Rock smashes scissor = You win")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cut the paper = Coputer win")
    else:
        print("Paper covers rock ,You win")
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes scissors,Computer win")
    else:
        print("Scissors cut the paper, You win")
