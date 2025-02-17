things = [True, 1.2, "Good", [1, 10]]
print(things[-2])
print("%".join([things[2][1:-1]]))
print([str(t)[0] for t in things])
print([len(str(t)) for t in things])
print([t for t in things if type(t) in (float, int)])
print([t for t in things if isinstance(t, int)])