
# Task 1: Write the user's name to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Task 2: Read the name from the file and print a greeting
with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Hi {name}!")

# Task 3: Add the first two numbers from numbers.txt and print the result
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
result = first_number + second_number
print(f"The sum of the first two numbers is: {result}")

# Task 4: Calculate the total of all numbers in numbers.txt
with open("numbers.txt", "r") as file:
    total = sum(int(line) for line in file)
print(f"The total of all numbers is: {total}")
