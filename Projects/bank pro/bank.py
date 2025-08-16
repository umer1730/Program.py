from datetime import datetime
import os
from colorama import Fore

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

daily_limit= 20000
loan_balance = 0
interest_rate = 5  # 5%
# username
user_name = input("Enter your username: ").strip()    # .strip()    is used to remove spaces
if not user_name:
    print("username can't be empty.")
    exit()
def file_path(name):
    return f"{user_name}_{name}.txt"
# pin
def load_pin():
    if not os.path.exists("pin.txt"):
        return None  # no pin set yet
    with open("pin.txt","r") as file:
        return file.read().strip()    
def save_pin(pin):
    with open("pin.txt","w") as file:
        file.write(pin)
# loan
def load_loan_balance():
    try:
        with open("loan.txt","r") as file:
            return float(file.read())
    except (FileNotFoundError, ValueError):
        return 0
def save_loan_balance():
    with open("loan.txt","w") as file:
        file.write(str(loan_balance))
# pin 
def verify_pin():
    stored_pin = load_pin()
    if stored_pin is None:
        new_pin=input("No Pin found.Set a new 4 digit pin: ")
        while not (new_pin.isdigit() and len(new_pin) == 4):
            new_pin = input("Invalid.Enter a 4 digit pin: ")
        save_pin(new_pin)
        print("Pin set successfully...")
        return True
    else:
        for _ in range(3):
            enterd_pin = input(Fore.BLUE+"Enter your pin: ")
            if enterd_pin == stored_pin:
                return True
            else:
                print("Incorrect pin.")
            print("Too many faled attempts.Existing....")
            return False
# change pin
def change_pin():
    stored_pin= load_pin()
    if stored_pin is None:
        print("No pin set.Please create one first.")
        return 
    current_pin = input("Enter current pin: ")
    if current_pin != stored_pin:
        print("Incorrect current pin.")
        return
    new_pin = input("Enter new 4 digit pin: ")
    confirm_pin = input("Confirm new pin: ")
    if new_pin != confirm_pin:
        print("Pin does not match")
        return
    elif not (new_pin.isdigit() and len(new_pin) == 4):
            print("Pin must be 4 digits.")
            return
    save_pin(new_pin)
    print("Pin changed successfully.")
# file hand
def load_balance():
    try:
        with open("balance.txt","r") as file:
            return float(file.read())
    except FileNotFoundError:
        return 0.0
    except ValueError:
        return 0.0

def save_balance():
    with open("balance.txt","w") as file:
        file.write(str(balance))

# daily withdraw
def load_daily_withdrawn():
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open("withdrawls.txt","r") as file:
            data=file.read().strip().split(",")
            if len(data) == 2 and data[0] == today:
                return float(data[1])
    except FileNotFoundError:
        pass
    return 0.0
def save_daily_withdrawn(amount):
    today = datetime.now().strftime("%Y-%m-%d")
    with open("withdrawls.txt","w") as file:
        file.write(f"{today},{amount}")

# transaction
def log_transaction(action,amount):
    now = datetime.now().strftime("%H:%M:%S %Y-%m-%d")
    with open("history.txt","a") as file:
        file.write(Fore.CYAN+f"[{now}] \t{action}: Rs.{amount:.2f}\n")

def show_history():
    try:
        with open("history.txt","r") as file:
            history=file.read()
            if history.strip() == "":
                print("No transaction history found.")
            else:
                print("Transaction history")
                print(history)
    except FileNotFoundError:
        print("No transaction history found.")
# functions
def show_balance():
    print(Fore.LIGHTBLACK_EX+f"Your balance is Rs.{balance:.2f}")
def deposit():
    amount = float(input(Fore.LIGHTWHITE_EX+"Enter an amount to be deposited: Rs."))
    if amount < 0:
        print(Fore.LIGHTWHITE_EX+"That's not a valid amount.")
        return 0
    else:
        print(Fore.MAGENTA+"Amount deposited successfully...")
        return amount
# withdraw

def withdraw():
    global daily_withdrawn
    amount = float(input(Fore.LIGHTWHITE_EX+"Enter amount to be withdrawn: Rs."))
    if amount > balance:
        print(Fore.LIGHTWHITE_EX+"Insufficient money...")
    elif amount <= 0:
        print(Fore.LIGHTWHITE_EX+"Amount must be greater then 0")
    elif daily_withdrawn + amount > daily_limit:
        print(Fore.LIGHTWHITE_EX+f"Sorry, daily withdrawl limit is Rs.{daily_limit}")
        return 0
    else:
        daily_withdrawn += amount
        save_daily_withdrawn(daily_withdrawn)
        print(Fore.MAGENTA+"Amount withdrawn successfully...")
        return amount
def transfer_money():
    global balance
    recipient_account= int(input(Fore.LIGHTWHITE_EX+f"Enter the recipient's account number: ")) 
    amount = float(input(Fore.LIGHTWHITE_EX+f"Enter amount to transfer: Rs.")) 
    if amount<= 0:
        print(Fore.LIGHTWHITE_EX+f"Amount must be greater then 0.")
    elif amount > balance:
        print(Fore.LIGHTWHITE_EX+f"Insufficient money.")
    else:
        print(Fore.LIGHTWHITE_EX+f"Rs.{amount:.2f} transferred to account {recipient_account} successfully.")
        return amount, recipient_account
#loan
def apply_loan():
    global balance,loan_balance
    amount = float(input("Enter loan amount: Rs."))
    if amount <= 0:
        print("Invalid amount.")
        return
    loan_balance += amount
    balance += amount
    print(f"Loan approved! Loan balance: Rs.{loan_balance:.2f}")
    save_loan_balance()
def repay_loan():
    global balance, loan_balance
    if loan_balance <= 0:
        print("No loan to repay.")
        return
    amount = float(input("Enter repayment amount: Rs."))
    if amount <= 0:
        print("Invalid repayment amount.")
        return
    if amount > balance:
        print("Insufficient amount to repay for loan.")
        return
    balance -= amount
    loan_balance -= amount
    if loan_balance <= amount:
        print("Loan fully repaid.")
        loan_balance = 0
    else:
        print(f"Remaining loan balance: Rs.{loan_balance:.2f}")
    save_loan_balance()
#bill

def bill_payment():
    global balance
    bills = {
        "1": "Electricity",
        "2": "Water",
        "3": "Internet",
        "4": "Gas"
    }
    print("Available bills to pay: ")
    for key, value in bills.items():
        print(f"{key}. {value}")
    choice = input("Selected bill types:  ")
    if choice not in bills:
        print("Invalid option.")
    amount = float(input(f"Enter amount for {bills[choice]} bill: Rs."))
    if amount <= 0:
        print("Invalid bill amount")
    elif amount > balance:
        print("Insufficient balance to pay the bill.")
    else:
        balance -= amount
        save_balance()
        log_transaction(f"Bill payment - {bills[choice]}", amount)
        print(f"{bills[choice]} bill of Rs.{amount:.2f} paid successfully.")

# main

if not verify_pin():
    exit()

balance = load_balance()
loan_balance = load_loan_balance()
daily_withdrawn = load_daily_withdrawn()

is_running = True

while True:
    clear_screen()
    print(Fore.GREEN+"-----------------------------------")
    print(Fore.GREEN+"#          Banking System         #")
    print(Fore.GREEN+"-----------------------------------")
    print(Fore.YELLOW+"1. Show Balance")
    print(Fore.YELLOW+"2. Deposit")
    print(Fore.YELLOW+"3. Withdraw")
    print(Fore.YELLOW+"4. Transfer money")
    print(Fore.YELLOW+"5. Show transaction history")
    print(Fore.YELLOW+"6. Apply for Loan")
    print(Fore.YELLOW+"7. Repay Loan")
    print(Fore.YELLOW+"8. Bill Payment")
    print(Fore.YELLOW+"9. Change Pin")
    print(Fore.YELLOW+"10.Exit")

    print(Fore.RED+"-------------------------------------")
    choice = input(Fore.RED+"Enter your choice: ")
    print(Fore.RED+"-------------------------------------")
    clear_screen()
    print()
    if choice == "1":
        print("----Balance----")
        show_balance()
    elif choice == "2":
        print("----Deposit----")
        amt=deposit()
        if amt > 0:   
            balance+=amt
            save_balance()
            log_transaction("Deposit",amt)
    elif choice == "3":
        print("----Withdraw----")
        amt = withdraw()
        balance -= amt
        save_balance()
        log_transaction("Withdraw",amt)
    elif choice == "4":
        print("----Transfer Money----")
        result= transfer_money()
        if result and len(result) == 2:
            amt, recipient_account = result
            balance -= amt
            save_balance()
            log_transaction(f"Transfer to {recipient_account}",amt)
    elif choice == "5":
        print("----Show transaction----")
        show_history()
    elif choice =="6":
        print("----Apply loan----")
        apply_loan()
    elif choice == "7":
        print("----Repay loan----")
        repay_loan()
    elif choice == "8":
        print("----Bill payment----")
        bill_payment()
    elif choice == "9":
        print("----Change Pin----")
        change_pin()
    elif choice == "10":
        is_running = False
        print("Thank you!")
        save_balance()
        save_loan_balance()
        break
    else:
        print(Fore.YELLOW+"This is not a valid statement....")
    input("Press Enter to return...")