length = int(input())
string = input()
indices = [int(i) for i in input().split()]
another_string = ""

for i in enumerate(string):
    
    if i[0] == indices[0]:
        if i[1].isupper():
            another_string += i[1].lower()
            continue
            
        elif i[1].islower():
            another_string += i[1].upper()
            continue
    
    if i[0] == indices[1]:
        if i[1].isupper():
            another_string += i[1].lower()
            continue
            
        elif i[1].islower():
            another_string += i[1].upper()
            continue
    
    another_string += i[1]

print(another_string)
