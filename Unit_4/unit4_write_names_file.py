names = input("Enter names separated by commas: ").split(",")
with open("names.txt", "w") as f:
    for name in names:
        f.write(name.strip() + "\n")
print("Names written to file.")
