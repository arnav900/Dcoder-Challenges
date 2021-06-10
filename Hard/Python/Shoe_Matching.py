n = int(input())
shoe, left, right = [], [], []      # creating lists to compare corresponding indices
counts = 0              # for counting the required number of pairs

for i in range(n):
    a, b = input().split()
    a = int(a)
    if a in shoe:       # if the shoe size is already present, we add the count in either the left or right list
        if b == "L":
            left[shoe.index(a)] += 1
        elif b == "R":
            right[shoe.index(a)] += 1
    else:               # if the shoe size appears for the first time while parsing the loop, we add a new element in each list for comparision
        shoe.append(a)
        left.append(0)
        right.append(0)
        if b == "L":
            left[shoe.index(a)] += 1
        elif b == "R":
            right[shoe.index(a)] += 1
            
for i in range(len(shoe)):
    if left[i] != 0 and right[i] != 0:          # if either R or L for a given size is not present, then we don't consider it as a pair can't be formed
        lists = [left[i], right[i]]
        counts += min(lists)                    # we take minimum of the right and left value as that represents the no. of complete pairs
    
print(counts)  
