n1 = int(input())
n2 = int(input())
r = None

while r != 0:
  r = n1 % n2
  n1, n2 = n2, r

print(n1)
