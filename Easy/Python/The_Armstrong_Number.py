num = input()
arr1 = [int(i) for i in num]
arr2 = [i ** 3 for i in arr1]

result = 0
for i in arr2:
  result += i

if result == int(num):
  print("YES")
else:
  print("NO")
