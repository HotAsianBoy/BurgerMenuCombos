"""Burger Combos v1
Simple input and print of dictionaries (list)"""


# A dictionary to store the combo meals with their details
combo_menu = {
    "Beef Burger": [("Beef Burger", 5.69), ("Fries", 1.00), ("Fizzy Drink", 1.00)],
    "Cheesy": [("Cheeseburger", 6.69), ("Fries", 1.00), ("Fizzy Drink", 1.00)],
    "Super": [("Cheeseburger", 6.69), ("Large Fries", 2.00), ("Smoothie", 2.00)]
}

# Print menu with spare lines for easier readability
for combo, items in combo_menu.items():
    print(f"Combo name: {combo}")
    print("Item and Price:")
    for item, price in items:
        print(f"{item} = ${price:.2f}")
    print()  # Print spare line

