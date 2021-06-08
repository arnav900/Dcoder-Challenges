arr = [int(i) for i in input().split() if i != -1]
arr.remove(-1)
for i in arr[::-1]:
  print(i, end=" ")
