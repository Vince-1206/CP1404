values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]
print(v)