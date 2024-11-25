# whitespace remover
# str
s=input("Enter a string: ")
c=s.strip()
if c==s:
    print("No whitespace to remove.")
else:
    print("Cleaned:", c)
