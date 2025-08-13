num = int(input("Enter the number: "))
miles = []
print("Enter the number of miles run in every saturday: ")
for i in range(num):
    miles.append(int(input()))  # int ki jo input ha usko append krdega

count = 0
for i in range(num-1):
    if miles[i+1] > miles[i]:
        count +=1
print(count) 

print()
print("---------L2-------")
print()

n = int(input("Enter the number: "))
ch = input("Enter the character: ")
ch =ch[0]
count = 0
for i in range(n):
    word=input(f"Enter word {i+1}:")
    for letter in word:
        if letter == ch:
            count +=1
print(count)

print()
print("---------L3-----")
print()

n = int(input("Enter the elements: "))
if n < 3:
    print("NO peak found")
else:
    arr=list(map(int,input("Enter the elements separated by space: ").split()))
is_found = False
print("Peak elements:", end=" ")
for i in range(1,n-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        print(arr[i],end=",")
        is_found=True
if not is_found:
    print("No peak found")

print()
print("-----------L4----------")
print()   

def is_repeating_cycle_length(length,arr,cycle_length):
    if cycle_length > length:
        return False
    for i in range(length):
        if arr[i] != arr[i % cycle_length]:
            return False
    return True
length = int(input("Enter the length: "))
arr= list(map(int,input(f"Enter {length} elements: ").split()))
cycle_length = int(input('Enter the cycle length:'))
result = is_repeating_cycle_length(length,arr,cycle_length)
print(result)

print()
print("-----------L5---------")
print()

total_volume=0
count=0
print("Enter box dimensions (length width height...) and -1 to stop: ")
dimensions = []
while True:
    try:
        num = int(input())
    except ValueError:
        print("Invalid input.Please enter integers only.")
        continue
    if num==-1:
        break
    dimensions.append(num)

if len(dimensions) % 3 != 0:
    print("Invalid input.Every box must have 3 dimensions. ")
else:
    for i in range(0,len(dimensions),3):
        length = dimensions[i]
        width = dimensions[i+1]
        height = dimensions[i+2]
        total_volume += length*width*height
    print(f"Total volume: {total_volume}")

print()
print("--------L6--------")
print()

size = 10
packages = []
print("Enter the wigths of the 10 packages: ")
for _ in range(size):
    packages.append(int(input()))

for i in range(size-1):
    for j in range(size-i-1):
        if packages[j] > packages[j+1]:
            packages[j], packages[j+1] = packages[j+1], packages[j]

print("sorted package weigths in ascending order:", end=" ")
for weigth in packages:
    print(weigth,end=" ")
