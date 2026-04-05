## TASK 1 - Explore the Menu

# The full menu data which is provided
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# List of categories in the order we want to display them
categories = ["Starters", "Mains", "Desserts"]

# Looping through each category and printing the items which belongs to that category
for category in categories :
    print(f"------ {category} ------")
    
    for item_name in menu :
        if menu[item_name]["category"] == category:
            price = menu[item_name]["price"]

            # Checking the avilability of the item
            if menu[item_name]["available"] == True:
                status = "[Available]"
            else :
                status = "[Unavailable]"

            # Printing the items neatly
            print(f"{item_name:<17} ₹{price:<10.2f} {status}") 
    print()

# The total number of items in the menu
total_items = len(menu)
print("Total items on the menu :", total_items)

# Counting the available items
available_count = 0
for item_name in menu :
    if menu[item_name]["available"] == True:
        available_count = available_count +1          
        
print("Total available items :", available_count)

# Finding the expensive item
expensive_item = ""
expensive_price = 0

for item_name in menu :
    if menu[item_name]["price"] > expensive_price:
        expensive_price = menu[item_name]["price"]
        expensive_item = item_name

print("Most expensive item :", expensive_item, "-", f"₹{expensive_price:.2f}")  

# Printing the items which are priced under 150
print("Items under ₹150:")
for item_name in menu:
    if menu[item_name]["price"] < 150:
        print(" -", item_name, "-", f"₹{menu[item_name]['price']:.2f}") 
                                                  
     


## TASK 2 - Cart Operations
# crating an empty cart
cart = []

# Function to add the item to the cart
def add_item(item_name, quantity):

    # Checking the availability of the item in the menu
    if item_name not in menu:
        print(f"'{item_name} is not on the menu.")
        return
    
    # Checking if the item is avvailable
    if menu[item_name]["available"] == False:
        print(f"'{item_name}' is currently unavailable.")
        return
        
    # Checking if item is already in the cart
    for entry in cart:
        if entry["item"] == item_name:

            # If the item is already in the cart, then increase the quantity
            entry["quantity"] = entry["quantity"] + quantity
            print(f"'{item_name}' quantity updated to {entry['quantity']}.")
            return                                                                                       

    # If the item is not in the cart yet, then add the item as new entry
    price = menu[item_name]["price"]
    cart.append({"item": item_name, "quantity": quantity, "price": price})
    print(f"'{item_name}' added to cart.")


# Function to remove the item from cart
def remove_item(item_name):

    # Looking for the item to remove from the cart
    for entry in cart:
        if entry["item"] ==item_name:
            cart.remove(entry)
            print(f"'{item_name}' removed from cart.")
            return
        
    # Item not found in cart
    print(f"'{item_name}' not found in cart.")

# Function to update the number of items in the cart
def update_quantity(item_name, new_quantity):

    # Looking for the item to update in the cart
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_quantity
            print(f"'{item_name}' quantity updated to {new_quantity}.")
            return
        
    # Item not found in cart
    print(f"'{item_name}' is not found in cart.")

# Function to print the current cart status
def print_cart():
    if len(cart) == 0:
        print("Cart is empty.")
    else:
        print("Current Cart:")
        for entry in cart:
            print(f" - {entry['item']} x {entry['quantity']} @ ₹{entry['price']:.2f}")


# --- simulating the sequence ---

print("\nAdding Paneer Tikka x2")
add_item("Paneer Tikka", 2)
print_cart()

print("\nAdding Gulab Jamun x1")
add_item("Gulab Jamun", 1)
print_cart()

print("\nAdding Paneer Tikka x1 (quantity should update to 3)")
add_item("Paneer Tikka", 1)
print_cart()

print("\nTrying to add Mystery Burger (does not exist in menu)")
add_item("Mystery Burger", 1)
print_cart()

print("\nTrying to add Chicken Wings (exists but unavailable)")
add_item("Chicken Wings", 1)
print_cart()

print("\nRemoving Gulab Jamun")
remove_item("Gulab Jamun")
print_cart()

# Final order summary
print("\n========== Order Summary ==========")

subtotal = 0
for entry in cart:
    item_total = entry["price"] * entry["quantity"]
    subtotal = subtotal + item_total
    print(f"{entry['item']:<20} x {entry['quantity']} ₹{item_total:.2f}") 
gst = round(subtotal * 0.05, 2)
total = round(subtotal + gst, 2)

print("-----------------------------------")
print(f"Subtotal:               ₹{subtotal:.2f}")
print(f"GST (5%):               ₹{gst:.2f}")
print(f"Total Payable:          ₹{total:.2f}")
print("===================================")




## TASK 3 - Inventory tracker with Deep Copy
import copy

# Making deep copy of inventiry before making any changes
inventory_backup = copy.deepcopy(inventory)

# To demonstrate how deep copy works, we will change the stock value
print("\n--Demonstrating Deep Copy--")
inventory["Paneer Tikka"]["stock"] = 999
print("After changing Paneer Tikka stock to 999:")
print("inventory stock:", inventory["Paneer Tikka"]["stock"])
print("inventory_backup stock:", inventory_backup["Paneer Tikka"]["stock"])

# Restocking the inventory to its original before contnuing
inventory["Paneer Tikka"]["stock"] = 10
print("Inventory restored back to original")

# Deducting quantities from inventory based on final cart
print("\n--Order Fulfillment--")
for entry in cart:
    item_name = entry["item"]
    quantity_needed = entry["quantity"]

    # Getting current stock for item
    current_stock = inventory[item_name]["stock"]

    # Checking the availability of the stock
    if current_stock >= quantity_needed:
        inventory[item_name]["stock"] = current_stock - quantity_needed
        print(f"{item_name}: Deducted {quantity_needed}. Stock left: {inventory[item_name]['stock']}")
    else:
        # If there is notenough stock - deduct only what is available
        print(f"Warning: Not enough stock for {item_name}. Only {current_stock} available. Deducting what we have.")
        inventory[item_name]["stock"] = 0

# Checking for any reorder alerts
print("\n-Reorder Alerts-")

for item_name in inventory:
    stock = inventory[item_name]["stock"]
    reorder = inventory[item_name]["reorder_level"]

    # If stock is at or below reorder level, print an alert
    if stock <= reorder:
        print(f"⚠ Reorder Alert: {item_name} Only {stock} unit(s) left (reorder level: {reorder})")

# Printing both inventory and backup to show the difference
print("\n-Confirming Deep Copy Protection-")
print("\nCurrent Inventory (after changes):")
for item_name in inventory:
    print(f"{item_name}: {inventory[item_name]['stock']} units")

print("\nInventory Backup (should be unchanged):")
for item_name in inventory_backup:
    print(f"{item_name}: {inventory_backup[item_name]['stock']} units")     




## TASK 4 - Daily Sales Log Analysis

#otal revenue per day
print("\n-- Daily Revenue --")

for date in sales_log:
    day_total = 0
    for order in sales_log[date]:
        day_total = day_total + order["total"]
    print(f"{date}: ₹{day_total:.2f}")

# Best selling day
best_day = ""
best_revenue = 0

for date in sales_log:
    day_total = 0
    for order in sales_log[date]:
        day_total = day_total + order["total"]
    if day_total > best_revenue:
        best_revenue = day_total
        best_day = date

print(f"\nBest Selling Day: {best_day} ₹{best_revenue:.2f}")

# Finding most ordered item
item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item not in item_count:
                item_count[item] = 0
            item_count[item] = item_count[item] + 1

most_ordered = ""
highest = 0

for item in item_count:
    if item_count[item] > highest:
        highest = item_count[item]
        most_ordered = item

print(f"Most Ordered Item: {most_ordered} ({highest} times)")

# Adding new day and reprinting the sales log
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\n--- Updated Daily Revenue ---")

best_day = ""
best_revenue = 0

for date in sales_log:
    day_total = 0
    for order in sales_log[date]:
        day_total = day_total + order["total"]
    print(f"{date}: ₹{day_total:.2f}")
    if day_total > best_revenue:
        best_revenue = day_total
        best_day = date

print(f"Updated Best Selling Day: {best_day} - ₹{best_revenue:.2f}")

# List of orders in numbered format
print("\n--All Orders--")
all_orders = []
for date in sales_log:
    for order in sales_log[date]:
        all_orders.append((date, order))

for number, (date, order) in enumerate(all_orders, 1):
    items = ", ".join(order["items"])
    print(f"{number}. [{date}] Order #{order['order_id']} - ₹{order['total']:.2f} - Items: {items}")


