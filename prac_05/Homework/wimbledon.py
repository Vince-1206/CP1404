"""
Estimate time: 30 minutes
Actual time: (to be updated after completion)
"""

import os

def read_wimbledon_data(filename):
    """Read the Wimbledon data from the given file and return a list of lists."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Error: The file '{filename}' was not found.")

    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    data = [line.strip().split(',') for line in lines[1:]]  # Skip header
    return data

def count_champions(data):
    """Count the number of wins per champion and return a dictionary."""
    champions = {}
    for entry in data:
        if len(entry) < 3:
            continue  # Skip malformed lines
        winner = entry[2]  # Assuming winner is in the third column
        champions[winner] = champions.get(winner, 0) + 1
    return champions

def get_countries(data):
    """Get a set of unique countries of champions."""
    countries = {entry[1] for entry in data if len(entry) > 1}  # Ensure correct indexing
    return countries

def main():
    """Main function to process data and display results."""
    filename = "wimbledon.csv"

    try:
        data = read_wimbledon_data(filename)
    except FileNotFoundError as e:
        print(e)
        return

    champions = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()

