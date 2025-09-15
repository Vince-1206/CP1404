# menu_program.py
"""
Menu-driven program that asks for a user's name and lets them choose
to be greeted with "hello" or "goodbye" until they choose to quit.
"""

# --- Get name from user ---
name = input("Enter name: ")

# --- Define menu string ---
MENU = "(H)ello\n(G)oodbye\n(Q)uit"

print(MENU)
choice = input(">>> ").upper()

# --- Menu loop ---
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")
