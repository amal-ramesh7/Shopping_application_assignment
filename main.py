
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
    with open("Orders.txt", "r") as Orders:
        for line in Orders:
            orderList.append(line.strip("\n"))
    #print(orderList)
    orderList = sorted(orderList, key=sortDates)
    #print(orderList)
    print("________________________________________")
    print(orderList[0])
    print("________________________________________")

def ordersByDate():
    orderList = []
    date = input("Enter the date in the format (YYYY-MM-DD): ")
    with open("Orders.txt", "r") as Orders:
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
            return

def main():
    previousOrders()

if __name__ == "__main__":
    print("Hello")
    main()



