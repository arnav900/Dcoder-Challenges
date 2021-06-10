n = int(input())
a = input().split()

a = [int(a[i]) for i in range(n)]   # converting to integer values

longli = []
for i in range(n):
    li = []   # logic: create nested lists that contain continuous positive or 0 elements and then check for max length
    for j in range(i, n):
        if a[j] >= 0:
            li.append(a[j])
        else:
            break     # if the element is negative, exit that loop and move on to next element
        longli.append(li)

maxi = []
for i in range(len(longli)):    # storing max length element (a list) as a new variable to print its elements later
    if len(longli[i]) > len(maxi):
        maxi = longli[i]

for i in maxi:
    print(i, end = " ")
