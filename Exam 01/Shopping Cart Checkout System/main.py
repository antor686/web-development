import os
products = {}

# This function takes valid quantity and price input from user 
def valid_input(text):
    
    while True:
        print(text,end="")
        value = input()
        try:
            value = float(value)
            return value
        except ValueError:
            print("Invalid input. Type numeric value (Ex: 10, 5,34)")

# This function clear the terminal for better interaction 
def clear_terminal():
    os.system('cls')
    print("-"*20,"Welcome to Shop", "-"*20)

# This function add items to cart 
def add_items(name, quantity, price):
    if name in products.keys():
        products[name]['quantity'] = products[name]['quantity'] + quantity
        products[name]['price'] = products[name]['price'] + price
    else:
        products[name] ={
            "quantity": quantity,
            "price" : price
        }

# This function shows the cart information         
def view_cart():
    print("{}{}{}".format("Product Name".ljust(20), "Quantity".ljust(10), "Price".ljust(10)))
    print("-"*40)
    for key, value in products.items():
        print(f"{key.ljust(20)}{str(value['quantity']).ljust(10)}{str(value['price']).ljust(10)}")
# This function does the checkout process 
def checkout(products):
    totalPrice = 0
    appliedDiscount = 0
    for key, value in products.items():
        totalPrice += value['price']

    if totalPrice >= 200:
      appliedDiscount = 0.10
    print("-"*20,end="")
    print("Checkout", end="")
    print("-"*20)
    view_cart()
    print("-"*40)
    print(f"{'Total Price :'.ljust(30)}{totalPrice}")
    print(f"{'Applied Discount :'.ljust(30)}{(totalPrice * appliedDiscount):.2f}")
    print(f"{'Net Total :'.ljust(30)}{(totalPrice - (totalPrice * appliedDiscount)):.2f}")

# This is the main program section 
flag = 1
while(flag):
    clear_terminal()
    print("What do you want to do?")
    print("1. Add Items To Your Cart.")
    print("2. View Your Shopping Cart.")
    print("3. Checkout")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    clear_terminal()
    if choice == 1:
        name = input("Enter Product Name: ")
        quantity = valid_input("Enter quantity: ")
        price = valid_input("Enter Price: ")
        add_items(name, quantity, price)
    elif choice == 2:
        view_cart()
        input()
    elif choice == 3:
        checkout(products)
        print("Continue Shopping? (Y/N): ",end="")
        choice = input()
        if choice == "Y" or choice == "y":
            flag = 1
        else:
            flag = 0
    elif choice == 4:
        flag = 0
    

