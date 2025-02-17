"""
names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))

name_to_remove = input("Who do you want to remove? ")

while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Name not in the list!")
    print(names)
    name_to_remove = input("Who do you want to remove?").title()
print("Good try!")

"""
"""
if name_to_remove in names:
    names.remove(name_to_remove)
    print(", ".join(names))
else:
    print(f"{name_to_remove} is not in the list.")
"""

"""
sum_of_number = 0
with open("number.txt", "r") as input_file:
    numbers = input_file.readlines()
    for number in numbers:
        sum_of_number += float(number)
    print(f"Total sum of numbers is {sum_of_number}")
"""


def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

"""
def main():
    numbers = get_numbers()
    squared_numbers = square_numbers(numbers)
    display_numbers(squared_numbers)
"""


