n = int(input())
string = input()
arr = []
for i in string:
  try:
    i = int(i)
    arr.append(i)
  except:
    continue
for i in arr:
  print(i, end=" ")
