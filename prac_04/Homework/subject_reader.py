"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data_list = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline characters
            parts = line.split(',')  # Split into components
            parts[2] = int(parts[2])  # Convert student count to an integer
            data_list.append(parts)  # Store in the list
    return data_list

def display_subject_details(data):
    """Display subject details in a formatted way."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()
