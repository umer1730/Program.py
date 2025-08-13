# PD 6

size=int(input("Enter the size of the fertilizer bag in in pounds: "))
bag=int(input("Enter the cost of the bag: "))
area=float(input("Enter the area in the square feet that can be covered by the bag: "))
cost= bag / size
print(f"Cost of fertilizers per pound: {cost}")
fertilizer= bag / area
print(f"Cost of fertilizer per squarefeet: {fertilizer}")

print()
# PD 7
print()

vegetables_price=float(input("Enter vegetable price in kilogram(in coin): "))
fruits_price=float(input("Enter fruit price in kilogram(in coin): "))
total_vegetables=float(input("Enter total kilograms of vegetables: "))
total_fruits=float(input("Enter total kilograms of fruits: "))
earnings = (vegetables_price * total_vegetables) + (fruits_price * total_fruits)
print(f"Total earnings in rupees: {earnings}")

print()
# PD 8
print()

name= input("Enter the name: ")
price_1=int(input("Enter the adult ticket price: "))
price_2=int(input("Enter the child ticket price: "))
adult= int(input("Enter the adult ticket sold: "))
child= int(input("Enter the children ticket sold: "))
percentage= float(input("Enter the percentage of the amount to be denoted charity: "))
total= (price_1 * price_2) + (price_2 * child)
donation = (total * percentage) / 100
remaining= total - donation
print(f"Total amount generated from ticket sales: ${total}")
print(f"Movie name: {name}")
print(f"Donation to charity(.10%): ${donation}")
print(f"Remaining amount after donation: ${remaining}")

print()
# PD 9
print()

num = int(input("Enter a 4 digit number: "))
digit_1 = num % 10
digit_2 = num % 10
digit_3 = num % 10
digit_4 = num % 10
sum = digit_1+digit_2 +digit_3 +digit_4
print(f"The sum of the digit is: {sum}")