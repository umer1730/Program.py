light = input("Enter color:")
if (light == "red"):
    print("stop")
elif (light == "yellow"):
    print("look")
elif (light == "green"):
    print("go")
else:
    print("error")
            
# even odd
def even_odd():
    num=int(input("Enter num:"))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    return num
user=even_odd()
print(user)