
word = input("Enter a string: ")
length = 0
for i in word:
    length += 1
if length%2==0:
    print("true")
else:
    print("false")

print()
print("_---------")
print()

def collatz_cycle_length(n):
    count= 1
    while (n != 1):
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
    return count
def main():
    n =int(input("Enter : "))
    cycle_length = collatz_cycle_length(n)
    print("Collatz Cycle Length: ",cycle_length)
if __name__ == "__main__":
    main()

print()
print("_---------")
print()

name= ""
name =input("Enter string: ")
length = 0
for i in name:
    length += 1
if length > 0 and name[length - 1] =="n":
    print("True")
else:
    print("False")

# we can also write............
# name = input("Enter a String: ")
# if len(name) > 0 and name[-1] == 'n':
#     print("true")
# else:
#     print("false")

