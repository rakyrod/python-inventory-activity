item_list = []
item_price = {}

def menuList():
    while True:
        print("===Inventory MENU===")
        print("[1] Add item")
        print("[2] Update price")
        print("[3] Exit")

        choice = input("Enter your choice: ")

        # add items
        if choice == "1":
            name = input("Enter item name: ").upper()

            if name in item_list:
                print("Invalid. Item already exists!")
            else:
                price = float(input("Enter Price: "))
                item_list.append(name)
                item_price[name] = price
                print("Item added!")

        # for update price
        elif choice == "2":
            name = input("Enter item name: ").upper()
            if name in item_list:
                updated_price = float(input("Enter new price: "))
                item_price[name] = updated_price
                print("Price updated!")
            else:
                print("Item not found!")

        # exit
        elif choice == "3":
            print("Exiting System..")
            break

        else:
            print("Invalid choice!")

# call the function so it will show up 
menuList()
