"""from fileinput import filename

in_file = open(filename,"r")
for line in in_file:
    if line sratwith("#")
        print(line.strip())
in_file.close()

"""

name = input("Name: ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
# out_file.close()
# print("Done")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)
print("Done")

