a=int(input("Enter The First Number : "))
b=int(input("Enter The Second Number : "))
c=a+b
d=a-b
e=a*b

print("==================")
print("|| Add is :",c,"||")
print("|| Sub is :",d,"||")
print("|| Mul is :",e,"||")

if b!=0 :
    f=a/b
    print("|| Div is :",f,"||")
    print("==================")
else :
    print("Number Not Divisible by Zero!!")
