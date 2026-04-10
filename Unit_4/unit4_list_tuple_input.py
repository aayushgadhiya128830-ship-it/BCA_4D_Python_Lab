values = input("Enter comma-separated numbers: ").split(",")
lst = [int(x) for x in values]
tpl = tuple(lst)
print("List:", lst)
print("Tuple:", tpl)
