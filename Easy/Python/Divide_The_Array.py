t = int(input())
arr = [int(i) for i in input().split()]

for i in enumerate(arr):
  if i[1] % 2 == 0 and i[0] % 2 == 1:
    print(i[1], end=" ")
