from collections import Counter

string = input()

s = Counter(string)

for i in s.keys():
  print(i, end="")
