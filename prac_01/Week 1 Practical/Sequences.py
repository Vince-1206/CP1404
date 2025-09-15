# sequences.py
"""
Menu-driven number sequence generator.
Allows the user to choose between displaying:
1. Even numbers from x to y
2. Odd numbers from x to y
3. Squares of numbers from x to y
4. Exit the program
"""

# --- Get range inputs from user ---
x = int(input("Enter the starting number (x): "))
y = int(input("Enter the ending number (y): "))

MENU = """\nNumber Sequence Generator
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y
4. Exit the program
"""

print(MENU)
choice = input("Enter your choice: ")

while choice != "4":
    if choice == "1":
        print("Even numbers:")
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()  # newline after sequence
    elif choice == "2":
        print("Odd numbers:")
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
    elif choice == "3":
        print("Squares:")
        for i in range(x, y + 1):
            print(i ** 2, end=" ")
        print()
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Enter your choice: ")

print("Finished. Goodbye!")
