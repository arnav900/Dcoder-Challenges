n = int(input())

if n > 0:
  for i in range(n + 1):
    if i == (n):
      print(2 ** i)
      continue
    print(2 ** i, end=",")

elif n < 0:
  print(1.0, end=",")
  i = -1
  while i >= n:
    if i == n:
      print(2 ** i, end="")
      break
    print(2 ** i, end=",")
    i -= 1

else:
  print(1)
