# A dictionary to store the combo meals with their details
combo_meals = {
    'Combo 1': {'items': ['Burger', 'Fries', 'Coke'], 'price': 5.99},
    'Combo 2': {'items': ['Chicken', 'Salad', 'Water'], 'price': 6.99},
    # Add more pre-existing combos here
}
def add_combo():
    name = input("Enter the name of the new combo: ")
    items = input("Enter the items in the combo separated by commas: ").split(',')
    price = float(input("Enter the price of the combo: "))
    combo_meals[name] = {'items': items, 'price': price}
    print("New combo added:", combo_meals[name])
    confirm = input("Is this information correct? (yes/no): ")
    if confirm.lower() == 'no':
        add_combo()

def search_combo():
    name = input("Enter the name of the combo to search: ")
    if name in combo_meals:
        print("Combo found:", combo_meals[name])
        confirm = input("Is this information correct? (yes/no): ")
        if confirm.lower() == 'no':
            update_combo(name)
    else:
        print("Combo not found.")

def update_combo(name):
    items = input("Enter the new items for the combo separated by commas: ").split(',')
    price = float(input("Enter the new price for the combo: "))
    combo_meals[name] = {'items': items, 'price': price}
    print("Combo updated:", combo_meals[name])

def delete_combo():
    name = input("Enter the name of the combo to delete: ")
    if name in combo_meals:
        del combo_meals[name]
        print(f"{name} has been deleted from the menu.")
    else:
        print("Combo not found.")

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