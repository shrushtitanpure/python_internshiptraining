####TASKK#####
# Initialize wallet balance
wallet_balance = 50000

def add_money(balance):
    amount = float(input("Enter amount to add: ₹"))
    balance += amount
    print(f"₹{amount} added successfully.")
    print(f"Updated Balance: ₹{balance}")
    return balance

def spend_money(balance):
    amount = float(input("Enter amount to spend: ₹"))
    if amount <= balance:
        balance -= amount
        print(f"₹{amount} spent successfully.")
    else:
        print("Insufficient balance!")
    print(f"Updated Balance: ₹{balance}")
    return balance

def check_balance(balance):
    print(f"Current Wallet Balance: ₹{balance}")
    return balance

# Main program loop
while True:
    print("\n--- E-Wallet Menu ---")
    print("Add money")
    print("Spend money")
    print("Check balance")
    print("Exit")

    choice = input("Choose an option: ").lower()

    if choice == "add money":
        wallet_balance = add_money(wallet_balance)

    elif choice == "spend money":
        wallet_balance = spend_money(wallet_balance)

    elif choice == "check balance":
        wallet_balance
