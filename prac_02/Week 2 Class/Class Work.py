"""
import random

# Ask user for input
low = int(input("Enter a low number: "))
high = int(input("Enter a high number: "))

# Ensure high > low
while high <= low:
    print("High number must be greater than low number!")
    high = int(input("Enter a high number: "))

# Generate random number between low and high
n = random.randint(low, high)

# Print n smiley faces
print(":)" * n)

"""

