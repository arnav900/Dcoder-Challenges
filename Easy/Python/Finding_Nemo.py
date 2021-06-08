n = int(input())
arr = input().split()
for i in enumerate(arr):
  if i[1] == 'Nemo':
    print(i[0] + 1)
  else:
    continue
