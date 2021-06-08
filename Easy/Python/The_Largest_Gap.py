t = int(input())
arr = [int(i) for i in input().split()]
max_num = arr[0]
min_num = arr[0]
for i in arr:
  if i > max_num:
    max_num = i

for i in arr:
  if i < min_num:
    min_num = i

print(max_num - min_num)
