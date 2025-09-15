# electricity_bill.py
"""
Electricity Bill Estimator
Calculates estimated electricity cost based on user input for price, daily usage, and billing days.
Then provides a second version that uses predefined tariffs.
"""

# ----- Version 1: Basic Estimator -----
print("Electricity bill estimator")
price_per_kwh = float(input("Enter cents per kWh: ")) / 100  # convert cents to dollars
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

bill = price_per_kwh * daily_use * billing_days
print(f"Estimated bill: ${bill:.2f}")

# ----- Version 2: Tariff-based Estimator -----
TARIFF_11 = 0.244618  # dollars per kWh
TARIFF_31 = 0.136928  # dollars per kWh

print("\nElectricity bill estimator 2.0")
tariff_choice = input("Which tariff? 11 or 31: ")
if tariff_choice == "11":
    price_per_kwh = TARIFF_11
elif tariff_choice == "31":
    price_per_kwh = TARIFF_31
else:
    print("Invalid tariff! Defaulting to Tariff 11.")
    price_per_kwh = TARIFF_11

daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

bill = price_per_kwh * daily_use * billing_days
print(f"Estimated bill: ${bill:.2f}")
