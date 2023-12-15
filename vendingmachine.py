price = int(input("Enter number: "))
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
    
    if price < 4:
        print("Thank you for your purchase, Come again!")
    elif price < 5:
        print("Thank you for your purchase, Come again!")
    elif price < 6:
        print("Thank you for your purchase, Come again!")
    elif price < 7:
        print("Thank you for your purchase, Come again!")
    elif price < 8:
        print("Thank you for your purchase, Come again!")
    elif price < 13:
        print("Thank you for your purchase, Come again!")
    elif price < 20:
        print("Thank you for your purchase, Come again!")
else:
    print("Invalid selection. Please enter a valid item number.")
