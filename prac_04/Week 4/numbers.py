def get_numbers():
    # Prompt the user to enter numbers separated by commas
    user_input = input("Enter numbers separated by commas: ")
    # Convert the input string into a list of floats
    numbers = [float(num.strip()) for num in user_input.split(",")]
    return numbers


def square_numbers(numbers):
    # Return a list of squared numbers
    return [num ** 2 for num in numbers]


def display_numbers(numbers):
    # Display the squared numbers
    print("This is a number which gives:", "..".join(f"{num:.2f}" for num in numbers))


main()