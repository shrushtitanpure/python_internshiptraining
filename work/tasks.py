##PS-Create a function that allows a users to recharge their moblie number

def mobile_recharge(mobile_number, amount):
    try:
        if not mobile_number.isdigit() or len(mobile_number) !=10:
            raise ValueError("Invalid mobile no . it must be 10 digits.")
        if amount<=10:
            raise ValueError("Reacharge amount must be more than rs 10")
        
        print(f"Recharge Successful!")
        print(f"Moblie Number:{mobile_number}")
        print(f"Amount Recharge :rs {amount}")
    except ValueError as e:
        print("Recharge faile!")
        print("Reaseon ",e)
        
        
mobile = input("Enter mobile number:")
try:
    recharge_amount = float(input("Enter recharge amount: "))
    mobile_recharge(mobile, recharge_amount)
except ValueError:
    print(" Please enter a valid numeric amount.")
    
    
#2:-ONLINE MOVIVE TICKET BOOKINGS
#PS- Create a funtion to book movie tikets.

def book_movie_tickets():
    TICKET_PRICE = 250
    MAX_TICKETS = 6

    try:
        tickets = int(input("Enter number of tickets: "))

        if tickets <= 0:
            raise ValueError("Number of tickets must be greater than zero.")

        if tickets > MAX_TICKETS:
            raise ValueError("You can book a maximum of 6 tickets only.")

        total_price = tickets * TICKET_PRICE

        print(" Booking Successful!")
        print(f"Tickets Booked: {tickets}")
        print(f" Total Price: ₹{total_price}")

    except ValueError as e:
        print("Booking Failed!")
        print("Reason:", e)


# Function call
book_movie_tickets()


#3:- Problem Statement:** Create a function to calculate electricity bill.

def calculate_electricity_bill():
    try:
        units = float(input("Enter electricity units: "))

        if units <= 0:
            raise ValueError("Units must be a positive number.")

        if units <= 100:
            bill = units * 5
        elif units <= 300:
            bill = units * 7
        else:
            bill = units * 10

        print("Bill Calculated Successfully!")
        print(f" Units Consumed: {units}")
        print(f" Total Bill Amount: ₹{bill}")

    except ValueError as e:
        print("Invalid Input!")
        print("Reason:", e)


# Function call
calculate_electricity_bill()








        