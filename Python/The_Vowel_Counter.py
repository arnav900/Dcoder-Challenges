string = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0

for i in string:
  if i in vowels:
    count += 1

print(count)
