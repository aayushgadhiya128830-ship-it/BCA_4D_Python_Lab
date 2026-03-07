a = int(input("Enter The Number For A : "))
b = int(input("Enter The Number For B : "))

print("=========================")

print("Before Swap A : ",a)
print("Before Swap B : ",b)

print("=========================")

print("Method : 1")
print()

c = a
a = b
b = c

print("After Swap A : ",a)
print("After Swap B : ",b)

print("=========================")

print("Method : 2")
print()

a = a+b
b = a-b
a = a-b

print("After Swap A : ",a)
print("After Swap B : ",b)

print("=========================")

print("Method : 3")
print()

a, b = b, a

print("After Swap A : ",a)
print("After Swap B : ",b)

print("=========================")
