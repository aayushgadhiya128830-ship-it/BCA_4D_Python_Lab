def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result
n = int(input("Enter The Number : "))
print("Factorial is : ",factorial(n))
