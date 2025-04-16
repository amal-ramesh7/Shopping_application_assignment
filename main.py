from datetime import datetime
import csv
import pandas as pd
import re

orders = []
def addProduct():
    
    print("----------------------------------------\nEnter \"back\" to move back to place order page\n----------------------------------------")
    price = 10 
    while True:
        with open("Data.csv", 'r') as file:
            data = csv.reader(file)
            headers = next(data)
            product_name = input("Enter the product name: ")
            found = False
            for row in data:
                items = []
                for item in row:
                    if '/' in item:
                        items.extend(each.strip(" ") for each in item.split("/"))
                    elif item=="":
                        continue
                    else:
                        items.append(item)
                if product_name in items:
                    found = True
                    with open("Orders.csv", 'a', newline="") as file:
                        writer = csv.writer(file)
                        found = True
                        quantity = int(input(f"How many {product_name} would you like to add?"))
                        cost = quantity*price 
                        current_date_time = datetime.now()
                        foramtted_date = current_date_time.strftime("%B %d %Y, %H:%M:%S.%f")
                        order = [foramtted_date, product_name, quantity, cost]
                        #file.write(",".join(map(str,order))+'\n')
                        writer.writerow(order)
                        break
        if product_name=='back':
            placeOrder()
        if not found:
            print(f"The product '{product_name}' is not available.")
        
def removeProduct():
    print("----------------------------------------\nEnter \"back\" to move back to place order page\n----------------------------------------")
    price = 10
    while True:
        item = input("What product would you like to remove from cart?")
        lines = []
        with open("Orders.txt", 'r') as f1:
            for row in f1:
                order = row.split(",")
                
                if item=="back":
                    placeOrder()
                elif item!=order[3]:
                    lines.append(row)
                else:
                    print(f"The product {item} removed from the orders")
        with open("Orders.txt",'w') as f2:
            f2.writelines(lines)


def placeOrder():
    action = int(input("\n1.Add product\n2.Remove product\n3.Back\nPlease choose the action to be performed:"))
    if action==1:
        addProduct()
    elif action==2:
        removeProduct()
    elif action==3:
        main()
    else:
        print("Enter a valid action")

def main():
    print("1. View Menu\n2. Place Order\n3. View History\n4. Exit")
    user_choice = int(input("Enter your choice: "))
    if user_choice==1:
        viewMenu()
    elif user_choice==2:
        placeOrder()
    elif user_choice==3:
        viewHistory()
    elif user_choice==4:
        exit()
    else:
        print("Enter a valid choice")

if __name__ == "__main__":
    print("Welcome to online shopping\n--------------------------\n")
    main()



