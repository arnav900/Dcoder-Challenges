bin_num = input()
arr = []

for i in bin_num:
  arr.append(i)

for i in range(len(arr)):
  if arr[i] == '1':
    arr[i] = '0'
  elif arr[i] == '0':
    arr[i] = '1'
  else:
    continue

for i in arr:
  print(i, end="")
 
