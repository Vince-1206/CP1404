import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    """Main function to run the program."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are the guitars:")
    display_guitars(guitars)

    print("\nSorting guitars by year...")
    guitars.sort()
    display_guitars(guitars)

    print("\nAdd new guitars:")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))

    save_guitars(filename, guitars)
    print("\nUpdated guitars saved!")


if __name__ == "__main__":
    main()

