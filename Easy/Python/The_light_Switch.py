s1, s2 = [int(i) for i in input().split()]

if s1 and s2:
    print(0)
elif not s1 and s2:
    print(1)
elif s1 and not s2:
    print(1)
else:
    print(0)
