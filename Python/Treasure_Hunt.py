c_of_bag = int(input())
max_v = 0
item1_v, item1_w = [int(i) for i in input().split()]
item2_v, item2_w = [int(i) for i in input().split()]

if item1_w + item2_w <= c_of_bag:
    print(item1_v + item2_v)
elif item1_v >= item2_v and item1_w <= c_of_bag:
    print(item1_v)
elif item2_w <= c_of_bag:
    print(item2_v)
else:
    print(0)
