# vowel count in string
s=input("Enter a string: ")
def count_vowels(s):
    return sum(1 for char in s if char in "aeiouAEIOU")
print("Vowel count:", count_vowels(s))
