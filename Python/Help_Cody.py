l = int(input())
arr = [int(i) for i in input().split()]

arr = sorted(arr, reverse=True)

for i in arr:
  print(i, end=" ")
