a = int(input("Enter The Marks For Subject 1 : "))
b = int(input("Enter The Marks For Subject 2 : "))
c = int(input("Enter The Marks For Subject 3 : "))
d = int(input("Enter The Marks For Subject 4 : "))
e = int(input("Enter The Marks For Subject 5 : "))

if a >=35 and b >=35 and c >=35 and d >=35 and e >=35 :
    f = a+b+c+d+e
    g = f/5
    print("======================")
    print("|| Total is || ",f,"||")
    print("|| Avg is   ||",g,"||")
    print("|| Result   || Pass ||")
    if g >= 90 :
        print("|| Grade is || A ||")
    elif g >= 75 :
        print("|| Grade is || B ||")
    elif g >= 65 :
        print("|| Grade is || C ||")
    elif g >= 50 :
        print("|| Grade is || D ||")
    elif g >= 40 :
        print("|| Grade is || E ||")
else :
    print("Result is Fail")
