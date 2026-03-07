n = int(input("Enter The Number : "))
num = n

power = len(str(n))
total = 0

while n > 0 :
    digit = n % 10
    total += digit ** power
    n //= 10
    
if total == num :
    print("Armstrong Number")
else :
    print("Not an Armstrong Number")
