n = int(input())
arr = [int(i) for i in input().split()]

result = 0
for i in arr:
  result += i

max_num = arr[0]
for i in arr:
  if i > max_num:
    max_num = i
print(result % max_num)
