with open("numbers.txt", "r") as f:
    nums = [float(line.strip()) for line in f]
total = sum(nums)
avg = total / len(nums)
print("Numbers:", nums)
print("Total:", total)
print("Average:", avg)
