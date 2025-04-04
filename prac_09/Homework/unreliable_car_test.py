"""
CP1404/CP5632 Practical
Test UnreliableCar class
"""
from prac_09.unreliable_car import UnreliableCar

# Create an unreliable car with 100 fuel and 30% reliability
unreliable_car = UnreliableCar("Old Banger", 100, 30)

# Attempt to drive the car multiple times
successful_drives = 0
attempts = 100
distance_per_attempt = 10

for _ in range(attempts):
    if unreliable_car.drive(distance_per_attempt) > 0:
        successful_drives += 1

# Print test results
print(f"Tried to drive {attempts} times, successful {successful_drives} times.")
print(unreliable_car)  # Print final state of the car
