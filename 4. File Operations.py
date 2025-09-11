# Writing to the file
names = ["Alice", "Bob", "Charlie", "Diana"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Reading from the file
with open("names.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line.strip())