# occurances of element in tuple
# tuple
t=tuple(input("Enter a list of items separated by commas: ").split(","))
e=input("Enter the element to count: ")
print(f"Occurrences of '{e}':", t.count(e))

