# Program to append (add) to the list[].
f = ['apple','banana','cherry']
f.append(input("Enter Something : "))
print(f)

# Progam to Extend(Marge) the List[].
f = ['apple','banana','cherry']
c = ['Ford','BMW','Volvo']
f.append(c)
print(f)

#program to insert an element at the specific position list[].
s = [43,45,77,50]
#inserting a new score at third position list[].
s.insert(int(input("Enter The Index : ")),int(input("Enter The Values : ")))
print(s)

#program to remove an element from the list[].
f1 = ['apple','banana','cherry']
f1.remove("banana")
print(f1)

#program to pop list element[].
f2 = ['apple','banana','cherry']
f2.pop()
print(f2)

#program to count occurrent of list element[].
f3 = ['apple','banana','cherry','apple','banana','cherry']
a_c = f3.count("apple")
print(a_c)

print(f"The Word 'apple' appears {a_c} times.")
