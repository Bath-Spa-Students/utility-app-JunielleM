print("""_  _ ____ _  _ ___  _ _  _ ____    _  _ ____ ____ _  _ _ _  _ ____ 
|  | |___ |\ | |  \ | |\ | | __    |\/| |__| |    |__| | |\ | |___ 
 \/  |___ | \| |__/ | | \| |__]    |  | |  | |___ |  | | | \| |___ 
                                                                   
""")
print("What would you like from the MENU?")
print("""Kitkat<1>, Snickers<2>, Mars<3>, Twix<4>, Maltesers<5>, Chupa Chups<6>, Skittles <7>, Mentos <8>, Sourpunk<9>, Airheads<10>, Cheetos<11>, Lays<12>, Tiffany<13>, Mr Krisps<14>, Doritos<15> """)
price = int(input("Enter the item number: "))
vending_machine = {
    # Chocolates
    '1': {'name': 'Kit-Kat', 'price': 2},
    '2': {'name': 'Snickers', 'price': 3},
    '3': {'name': 'Mars', 'price': 4},
    '4': {'name': 'Twix', 'price': 2.5},
    '5': {'name': 'Maltesers', 'price': 5},
    # Candies
    '6': {'name': 'Chupa Chups', 'price': 1.5},
    '7': {'name': 'Skittles', 'price': 2},
    '8': {'name': 'Mentos', 'price': 1},
    '9': {'name': 'SourPunk', 'price': 1.8},
    '10': {'name': 'Airheads', 'price': 2.5},
    # Chips
    '11': {'name': 'Cheetos', 'price': 3},
    '12': {'name': 'Lays', 'price': 2.5},
    '13': {'name': 'Tiffany', 'price': 2},
    '14': {'name': 'Mr Krisps', 'price': 1.5},
    '15': {'name': 'Doritos', 'price': 3},
}

selected_item = vending_machine.get(str(price))

if selected_item:
    item_name = selected_item['name']
    item_price = selected_item['price']
    print(f"You selected: {item_name}. Price: ${item_price}")
# Confirmation of the product you want to purchase
    confirmation = input(f"Do you want to purchase {item_name}? (yes/no): ").lower()
    if confirmation == 'yes':
        payment_method = input("Choose payment method (cash/card): ").lower()
        if payment_method == 'cash':
            print("Please insert cash into the machine.")
        elif payment_method == 'card':
            print("Please insert your card into the card reader.")
        else:
            print("Invalid payment method. Purchase canceled. Have a nice day!")
            exit()

        # Receipt after purchase
        print("\n-------- Receipt --------")
        print(f"Item: {item_name}")
        print(f"Price: ${item_price}")
        print(f"Payment Method: {payment_method.capitalize()}")
        print("-------------------------")

        print("Thank you for your purchase! Come again!")
    else:
        print("Purchase canceled. Have a nice day!")
else:
    print("Invalid selection. Please enter a valid item number.")
