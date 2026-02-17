#write a program to print all number which are divisible by 7 between 1 to 200

a = int(input("Emter The Number : "))
n = int(input("Emter The Range : "))

for i in range(1,n+1) :
    if i%a==0 :
        print(i)
