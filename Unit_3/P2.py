n = int(input("Enter The Number : "))
flag = 0
for i in range(2,n) :
    if n%i==0 :
        flag = 1
        break
if flag == 1 :
    print("Number",n,"is Not Prime")
else :
    print("Number",n,"is Prime")
