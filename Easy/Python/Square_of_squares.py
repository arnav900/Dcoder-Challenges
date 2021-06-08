from math import sqrt

num = int(input())
if sqrt(abs(num)) ** 2 == num:
  print("YES")
else:
  print("NO")
