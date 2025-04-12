monsters = [
    ["Mike", 340, "blue"],
    ["James", 14, "green"],
    ["Randall", 24, "purple"]
]

scary_monsters = [monster for monster in monsters if monster[1] > 20]

print(scary_monsters)