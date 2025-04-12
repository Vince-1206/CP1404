"""
Hexadecimal Colour Lookup
Estimate: 15 minutes
Actual:
"""

HEX_COLOURS = {
    "Amber": "#FFb00",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF",
}

colour_name = input("Enter colour name: ").strip().title()
while colour_name:
    try:
        print(f"{colour_name} is {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().title()
