# shop_calculator.py
"""
Shop Calculator Program
Allows the user to enter the number of items and their prices,
then calculates and displays the total price.
If the total price is over $100, a 10% discount is applied.
"""

# --- Input with Validation ---
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# --- Main Calculation ---
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# --- Discount if total > $100 ---
if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

# --- Output ---
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
