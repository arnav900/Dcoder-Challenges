n = int(input())
l, mi, ma = [], [], []

for i in range(n):
    x, y = input().split()
    mi.append(int(x))
    ma.append(int(y))
    
mi.sort()
ma.sort()

happy_result = 1
happy_stu = 1
books = mi[0]

i = 1
j = 0
while (i < n and j < n):
    if mi[i] <= ma[j]:
        happy_stu += 1
        i += 1
    elif mi[i] > ma[j]:
        happy_stu -= 1
        j += 1
    if happy_stu > happy_result:
        happy_result = happy_stu
        books = mi[i - 1]

print(books, happy_result)
