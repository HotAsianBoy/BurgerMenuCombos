"""Burger Combos v2
Completed code without Easygui, using definitive list and functions
as well as while loops, however loop only ends when user decides to
exit the program"""
# List of each combo meal and price for each
combo_meals = {
    'Combo 1 = Value': {'items': ['Beef Burger', 'Fries', 'Fizzy Drink'], 'price': 6.69},
    'Combo 2 = Cheesy': {'items': ['Cheese Burger', 'Fries', 'Fizzy Drink'], 'price': 8.69},
    'Combo 3 = Super': {'items': ['Cheese Burger', 'Large Fries', 'Smoothie'], 'price': 10.69}
}


# Allows the user to add combo wanted as well as asking if the new combo input has the correct info
def add_combo():
    name = input("Enter the name of the new combo: ")
    items = input("Enter the items in the combo separated by commas: ").split(',')
    price = float(input("Enter the price of the combo: "))
    combo_meals[name] = {'items': items, 'price': price}
    print("New combo added:", combo_meals[name])
    confirm = input("Is this information correct? (yes/no): ")
    if confirm.lower() == 'no':
        add_combo()


# Allows the user to search for a combo already from the list
def search_combo():
    name = input("Enter the name of the combo to search: ")
    if name in combo_meals:
        print("Combo found = ", combo_meals[name])
        confirm = input("Is this information correct? (yes/no): ")
        if confirm.lower() == 'no':
            update_combo(name)
    else:
        print("Combo not found.")


# Updates the list and adds the new combo from the user
def update_combo(name):
    items = input("Enter the new items for the combo separated by commas: ").split(',')
    price = float(input("Enter the new price for the combo: "))
    combo_meals[name] = {'items': items, 'price': price}
    print("Combo updated:", combo_meals[name])


# Allows the user to delete a combo if necessary
def delete_combo():
    name = input("Enter the name of the combo to delete: ")
    if name in combo_meals:
        del combo_meals[name]
        print(f"{name} has been deleted from the menu.")
    else:
        print("Combo not found.")


# Allows the user to see the full menu list after editing or observing
def print_menu():
    print("Full Combo Menu:")
    for name, details in combo_meals.items():
        items_str = ', '.join(details['items'])
        print(f"{name}: {items_str} - ${details['price']}")


# Main loop
while True:
    print("\nOptions:")
    print("1 - Add a new combo meal")
    print("2 - Search for an existing combo meal")
    print("3 - Delete a combo meal")
    print("4 - Display the full menu")
    print("5 - Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_combo()
    elif choice == '2':
        search_combo()
    elif choice == '3':
        delete_combo()
    elif choice == '4':
        print_menu()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")
