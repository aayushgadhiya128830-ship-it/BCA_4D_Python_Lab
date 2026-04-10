n = int(input("Enter n: "))
import math
result = {i: math.sqrt(i) for i in range(1, n+1)}
print(result)
