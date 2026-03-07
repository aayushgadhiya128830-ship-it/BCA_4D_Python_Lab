a = int(input("Enter The Number : "))

print("======================")
print("Method : 1")
b = str(a)
c = b[::-1]
d = int(c)

print("After Rev. Number : ",d)

print("======================")
print("Method : 2")
b = int(str(a)[::-1])

print("After Rev. Number : ",b)
