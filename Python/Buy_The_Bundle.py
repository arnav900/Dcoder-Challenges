t = int(input())

while t:
  
  no_of_s, no_of_b = [int(i) for i in input().split()]
  
  if no_of_b % no_of_s == 0:
    print("Yes")
  else:
    print("No")
  
  t -= 1
