ages = [int(i) for i in input().split()]

max_age = ages[0]

for i in ages:
  if i > max_age:
    max_age = i

print(max_age)
