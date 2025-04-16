from datetime import datetime
import csv
import pandas as pd
import re


#Displays the list when the user enters view menu option 
def view_menu():
    print(" Enter the option to view menu: 1-Filter items(edible/non-edible) 2-Display all items   3-Exit from menu")
    menu_choice=int(input())
    if menu_choice==1:
        display_filter_items()
    elif menu_choice==2:
        display_all_items()
    elif menu_choice==3:
        main()
    else:
        print("Please enter the valid input.")
        main()


#Displays filtered items when user enters option-1 
def display_filter_items():
    print("Enter the filter for 1- edible 2-non-edible:")
    display_choice=int(input())
    edible_headers = ["Fresh vegetables", "Condiments / Sauces", "Baked goods", "Fresh fruits"]
    non_edible_headers=["Personal care",	"Cleaning products", "Baby stuff"]
    # Create a dictionary for each category
    edible = {header: [] for header in edible_headers} 
    non_edible={header: [] for header in non_edible_headers}

    #some edible keywords that might be under non-edible header
    edible_keywords = ["food", "formula", "vitamin", "supplement"]

    #access the csv
    with open("Data.csv","r") as file:
        #read as the list format(iterable)
        data=csv.reader(file)
        headers = next(data)
        for row in data:
            #get its index using enumerate to access the header
            for i, item in enumerate(row):
                if item.strip() == "":
                    continue
                if headers[i] in edible_headers or any(keyword in item.strip().lower() for keyword in edible_keywords):
                    if headers[i] not in edible:
                        edible[headers[i]]=[]
                    edible[headers[i]].append(item.strip())
                else:
                    non_edible[headers[i]].append(item.strip())
                    
    if display_choice==1:
        for category, items in edible.items():
            print(f"\n{category}:")
            for item in items:
                print(item)
        #return to the view menu
        view_menu()
    elif display_choice==2: 
        for category, items in non_edible.items():
            print(f"\n{category}:")
            for item in items:
                print(item)
        #return to the view menu
        view_menu()
    else:
        print("Enter the correct choice.")
        #return to the view menu
        view_menu()

#Displays all the items when user enters option-2 
def display_all_items():
     with open("Data.csv","r") as file:
        #read as the list format(iterable)
        data=csv.reader(file)
        headers = next(data)
        menu_list={header:[] for header in headers}
        for row in data:
            for i,item in enumerate(row):
                if item.strip()=="":
                    continue
                menu_list[headers[i]].append(item.strip())
        for category, items in menu_list.items():
            print(f"\n{category}:")
            for item in items:
                print(item)

        #return to the view menu
        view_menu()



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
                        foramtted_date = current_date_time
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
        with open("Orders.csv", 'r') as f1:
            for row in f1:
                order = row.split(",")
                
                if item=="back":
                    placeOrder()
                elif item!=order[1]:
                    lines.append(row)
                else:
                    print(f"The product {item} removed from the orders")
        with open("Orders.csv",'w') as f2:
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

def sortDates(orderList):
    split = orderList.split(",")
    date= split[0].split(" ")[0].split("-")
    time = split[0].split(" ")[1].split(":")
    dT = "".join(date) + "".join(time)
    #print(dT)
    return (dT)
#Comment

def recentOrder():
    orderList = []
    with open("Orders.csv", "r") as Orders:
        for line in Orders:
            orderList.append(line.strip("\n"))
    #print(orderList)
    orderList = sorted(orderList, key=sortDates)
    #print(orderList)
    print("________________________________________")
    print(orderList[-1])
    print("________________________________________")

def ordersByDate():
    orderList = []
    date = input("Enter the date in the format (YYYY-MM-DD): ")
    with open("Orders.csv", "r") as Orders:
        for line in Orders:
            orderList.append(line.strip("\n"))
    
    print("________________________________________")
    for order in orderList:
        if date in order:
            print(order)
            continue
    print("________________________________________")


def previousOrders():
    while True:
        print(
"""----------------------------------------
Enter \"back\" to move back to place order page
----------------------------------------""")
        
        choice =input("""
1. View most recent order
2. Check order by date
Choice: """)
        if choice == "1":
            recentOrder()
            pass
        elif choice == "2":
            ordersByDate()
            pass
        elif choice == "back":
            main()

def main():
    print("1. View Menu\n2. Place Order\n3. View History\n4. Exit")
    user_choice = int(input("Enter your choice: "))
    if user_choice==1:
        view_menu()
    elif user_choice==2:
        placeOrder()
    elif user_choice==3:
        previousOrders()
    elif user_choice==4:
        exit()
    else:
        print("Enter a valid choice")

if __name__ == "__main__":
    print("Welcome to online shopping\n--------------------------\n")
    main()






