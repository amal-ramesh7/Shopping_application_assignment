import csv

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





       


def main():
    print("Enter the choice :1-View menu   2-Place order 3-View order   4-Exit :")
    choice=int(input())
    if choice==1:
        view_menu()
    elif choice==2:
        place_order()
    elif choice==3:
        view_order()
    elif choice==4:
        exit()
    else:
        print("Please enter the valid input.")
        exit()


if __name__ == "__main__":
    main()






