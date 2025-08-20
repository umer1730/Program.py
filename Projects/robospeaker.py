import os
if __name__== "__main__":
    print("Welcome to RoboSpeaker 1.1 create by Umer")
    while True:
        x=input("Enter what you want: ")
        if x == "quit":
            break
        command=f"say{x}"
        os.system(command)