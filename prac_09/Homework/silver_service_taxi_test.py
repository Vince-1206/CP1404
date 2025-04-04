"""
CP1404/CP5632 Practical
Test SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi with name "Hummer", 200 fuel, and fanciness of 2
luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Drive 18 km
luxury_taxi.drive(18)

# Print the taxi's details
print(luxury_taxi)

# Check fare calculation
fare = luxury_taxi.get_fare()
print(f"Total fare: ${fare:.2f}")

# Assert test to ensure correct fare calculation
assert round(fare, 2) == 48.78, "Fare calculation is incorrect!"
