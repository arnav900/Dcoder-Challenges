t = int(input())

while t:
  
  angles = [int(i) for i in input().split()]
  if sum(angles) == 360:
    print("YES")
  else:
    print("NO")
  
  t -= 1
