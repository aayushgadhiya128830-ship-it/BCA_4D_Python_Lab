a = int(input("Enter The Age : "))

if a<12 :
    print("You Are Kid")
elif a>=12 and a<=17 :
    print("You Are Teenager")
elif a>=18 and a<60 :
    print("You Are Adult")
elif a>=60 :
    print("You Are Senior Citizen")
else :
    print("Enter Valid Age!!")
