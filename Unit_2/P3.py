a = input("Enter The Letter : ").lower()

if a.isalpha and len(a) == 1 :
    if a in "aeiou" :
        print("Letter",a,"=> is Vowel")
    else :
        print("Letter",a,"=> is Consonent")
else :
    print("Enter a Single Letter!!")
