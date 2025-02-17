"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A: ValueError will occur if the user enters a non-integer
   input for either the numerator or the denominator.

2. When will a ZeroDivisionError occur?
A: ZeroDivisionError will occur if the denominator
   is entered as 0 and the division is attempted.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A: Yes, by adding a check to ensure the denominator is not
   zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Check for ZeroDivisionError before attempting division
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Please enter a non-zero denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")