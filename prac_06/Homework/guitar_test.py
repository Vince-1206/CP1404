"""
Estimate time: 10 minutes
Actual time: 15
"""

from guitar import Guitar

def main():
    """Test the Guitar class methods."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 500)

    print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 11. Got {another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()
