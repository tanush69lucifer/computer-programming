# checking if string contains digit
# str
s=input("Enter a string: ")
d=s.isdigit()
if not d:
    print("String does not contain only digits.")
else:
    print("Contains only digits:", d)
