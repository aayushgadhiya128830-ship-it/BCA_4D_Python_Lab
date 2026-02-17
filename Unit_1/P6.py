p=int(input("Enter The Amount : "))
r=int(input("Enter The Rate : "))
t=int(input("Enter The Time : "))
a=p * (1+r/100) ** t
ci=a-p
print("Compound Int is : ",ci)
