import os
sales = []
summary = {}

# This function takes valid quantity and price input 
def get_valid_input(text):
    while True:
        try:
            value = float(input(text))
            if value > 0:
                return value
            else:
                print("Value must be greater than 0")
        except ValueError:
            print("Invalid input. Enter numeric values (Ex: 20, 35, 3)")

# This function takes sales information from user 
def get_sales_info():
    while True:
        item = input("Enter item name or 'done' to finish: ")
        if item.lower() == 'done':
            break
        quantity = get_valid_input("Enter quantity: ")
        unit_price = get_valid_input("Enter unit price: ")
        sales.append((item, quantity, unit_price))

# This function calculate revenue from sales data 
def revenue_calculate(sales):
    for item, quantity, price in sales:
        revenue = quantity * price
        if item in summary:
            summary[item]["unit_sold"] += quantity
            summary[item]["revenue"] += quantity

        else:
            summary[item] = {
                "unit_sold" : quantity,
                "unit_price" : price,
                "revenue" : revenue
            }
# This function generate sales summary 
def generate_summary(summary):
    print("-"*10,"Daily Sales Summary", "-"*10)
    print(f"{'Item Name' .ljust(20)}{'Quantity'.ljust(10)}{'Unit Price'.ljust(15)}{'Revenue'.ljust(15)}")
    for item, info in summary.items():
        print(f"{item.ljust(20)} {info['unit_sold']:<10} {info['unit_price']:<10}{info['revenue']:>10}")

#This function clear the termal for better interaction
def clear_terminal():
    os.system('cls')
    print("-"*20,"Welcome To Daily Sales Report Generator","-"*20)


# This is the main program section
flag = 1
while flag:
    clear_terminal()
    print("1. Enter Sales Data.")
    print("2. View Sales Summary")
    print("3. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        clear_terminal()
        get_sales_info()
        
    elif choice == 2:
        clear_terminal()
        revenue_calculate(sales)
        generate_summary(summary)
        input()
    elif choice == 3:
        flag = 0
    else:
        continue

    
