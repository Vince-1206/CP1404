"""
CP1404/CP5632 Practical
Taxi Simulator
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    current_taxi = None
    total_bill = 0.0

    while True:
        print("\nq)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display available taxis and let the user select one."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    """Drive the selected taxi and return the fare for the trip."""
    distance = float(input("Drive how far? "))
    taxi.start_fare()  # Reset fare before each trip
    taxi.drive(distance)
    fare = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${fare:.2f}")
    return fare


def display_taxis(taxis):
    """Display the list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
