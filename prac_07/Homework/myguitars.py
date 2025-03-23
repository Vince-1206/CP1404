import csv
from guitar import Guitar


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row[0], int(row[1]), float(row[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
    return guitars


def save_guitars(filename, guitars):
    """Write guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("Current guitars:")
    display_guitars(guitars)

    print("\nSorting guitars by year...")
    guitars.sort(key=lambda g: g.year)
    display_guitars(guitars)

    print("\nEnter new guitars (or press enter to finish):")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))

    save_guitars(filename, guitars)
    print("Guitars saved successfully.")


if __name__ == "__main__":
    main()
