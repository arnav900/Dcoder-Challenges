l, h, d = [int(i) for i in input().split()]
count = 0

for i in range(l, h + 1):
  if i % d == 0:
    count += 1

print(count)
