import os
import datetime
from colorama import Fore, Style, init
init(autoreset=True)

MENU = {
    "pizza": {
        "maggi pizza": 300,
        "bbq chicken pizza": 500,
        "peri peri pizza": 600,
        "chicken fajitha pizza": 600,
        "afghani tikka pizza": 600,
        "behari chicken pizza": 400
    },
    "sandwich": {
        "club sandwich": 350,
        "Egg salad": 350,
        "Cheese sandwich": 350,
        "Grilled sandwich": 350,
        "Bbq sandwich": 400,
        "Cuban sandwich": 450
    },
    "burger": {
        "zinger burger": 300,
        "beef burger": 500,
        "cheese burger": 350,
        "chicken burger": 200,
        "anda shami burger": 150,
        "double patty burger": 400
    },
    "fries": {
        "regular fries": 100,
        "masala fries": 120,
        "cheese fries": 150,
        "loaded fries": 200,
        "achari fries": 150,
        "crinkle fries": 180
    },
    "ketchup": {
        "tomato ketchup": 0,
        "chilli ketchup": 0
    },
    "coffee": {
        "espresso": 180,
        "cappuccino": 220,
        "cold coffee": 250,
        "americano": 250,
        "long black": 250,
        "irish coffee": 250
    },
    "drinks": {
        "coke": 100,
        "sprite": 100,
        "pepsi": 100,
        "tea": 100 
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    print(Fore.YELLOW + "----------------------------------------------------")
    print(Fore.GREEN + "#             WELCOME TO OUR RESTAURANT            #")
    print(Fore.YELLOW + "----------------------------------------------------")
    print(Fore.CYAN + "--------- MENU ---------")
    for i, category in enumerate(MENU.keys(), 1):
        print(Fore.BLUE + f"{i}. {category.replace('_', ' ').title()}")
    print(Fore.BLUE + f"{len(MENU) + 1}. Show Bill & Checkout")
    print(Fore.CYAN + "-----------------------------")

def display_sub_menu(category_name):
    if category_name not in MENU:
        print(Fore.RED + "Invalid category.")
        return

    print(Fore.MAGENTA + f"\n--- {category_name.replace('_', ' ').title()} Menu ---")
    items = MENU[category_name]
    for i, (item, price) in enumerate(items.items(), 1):
        if category_name == "ketchup":                     # ketchup give free 
            print(Fore.YELLOW + f"{i}. {item.title()}: Comes free with all items.")
        else:
            print(Fore.CYAN + f"{i}. {item.title()}: Rs.{price:.2f}")
    print(Fore.MAGENTA + "----------------------------")

def get_item_details(category_name, item_choice):
    items = list(MENU[category_name].items())
    if 1<=item_choice<=len(items):
        item_name, item_price=items[item_choice - 1]
        return item_name, item_price
    return None, None

def take_customer_order():
    ordered_items = []
    while True:
        clear_screen()
        display_main_menu()

        try:
            main_choice=int(input(Fore.WHITE + "Enter your option: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            input(Fore.YELLOW + "Press Enter to continue...")
            continue

        if main_choice == len(MENU) + 1:
            break

        main_categories = list(MENU.keys())
        if 1 <= main_choice <= len(main_categories):
            selected_category_name = main_categories[main_choice - 1]
            clear_screen()
            display_sub_menu(selected_category_name)

            while True:
                try:
                    item_choice = input(Fore.WHITE + f"Enter the number of the {selected_category_name.title()} item (or '0' to go back): ")
                    item_choice = int(item_choice)

                    if item_choice == 0:
                        break

                    item_name, item_price = get_item_details(selected_category_name, item_choice)

                    if item_name:
                        quantity_input = input(Fore.WHITE + f"How many {item_name.title()} would you like? (Enter a number): ")
                        try:
                            quantity = int(quantity_input)
                            if quantity > 0:
                                ordered_items.append((item_name.title(), item_price, quantity))
                                print(Fore.GREEN + f"{quantity} x {item_name.title()} added to your order.")
                            else:
                                print(Fore.RED + "Quantity must be a positive number.")
                        except ValueError:
                            print(Fore.RED + "Invalid quantity. Please enter a number.")
                    else:
                        print(Fore.RED + "Invalid item number. Please try again.")
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a number.")

                add_more = input(Fore.YELLOW + "Add another item from this category? (yes/no): ").lower()
                if add_more != 'yes':
                    break
        else:
            print(Fore.RED + "Invalid menu option. Please select a valid number.")
            input(Fore.YELLOW + "Press Enter to continue...")

    return ordered_items

def generate_bill(ordered_items):
    clear_screen()
    now=datetime.datetime.now()
    date_time_str=now.strftime("%H:%M:%S %p %m-%Y")
    print(Fore.YELLOW+"========== YOUR BILL ==========")
    print(Fore.WHITE+f"Date & Time: {date_time_str}")
    print(Fore.WHITE+"================================")
    if not ordered_items:
        print(Fore.RED+"You have not ordered any items.")
        print(Fore.YELLOW+"=============================")
        return
    total_bill=0.0
    total_items=0
    print(Fore.GREEN+"----Ordered Items----")
    for item_name,price,quantity in ordered_items:
        line_total=price*quantity
        total_bill += line_total
        total_items += quantity
    print(Fore.GREEN + "--------------------")
    print(Fore.CYAN + f"Total Items: {total_items}")
    print(Fore.CYAN + f"Subtotal: Rs.{total_bill:.2f}")

    # giv discount if total exceeds 1000
    discount = 0
    if total_bill > 1000:
        discount= total_bill * 0.05  # 5% discount
        print(Fore.GREEN + f"Discount (5%): -Rs.{discount:.2f}")

    final_total = total_bill - discount
    print(Fore.CYAN + f"Total Payable: Rs.{final_total:.2f}")
    print(Fore.YELLOW + "=============================")
    print(Fore.GREEN + "Thank you for your order! Visit us again.")

def main():
    clear_screen()
    print(Fore.GREEN + "Welcome to our Restaurant!")
    customer_order = take_customer_order()
    generate_bill(customer_order)

if __name__ == "__main__":
    main()
