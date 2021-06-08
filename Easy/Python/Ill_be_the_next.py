from string import ascii_lowercase, ascii_uppercase

letters_upper = [i for i in ascii_uppercase]
letters_lower = [i for i in ascii_lowercase]
string = input()
another_string = ""

for i in string:
    if i.islower():
        another_string += letters_lower[letters_lower.index(i) + 1]
        continue
    
    if i.isupper():
        another_string += letters_upper[letters_upper.index(i) + 1]
        continue
        
print(another_string)
