garry = [int(i) for i in input().split()]
sharry = [int(i) for i in input().split()]

garry_sum = sum(garry)
sharry_sum = sum(sharry)

if garry_sum == sharry_sum:
    print(None, 0)
elif garry_sum < sharry_sum:
    print("Sharry", sharry_sum - garry_sum)
elif garry_sum > sharry_sum:
    print("Garry", garry_sum - sharry_sum)
else:
    pass
