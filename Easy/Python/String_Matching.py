t = int(input())

while t:
  string1, string2 = input().split()
  
  if string2 in string1:
    print("Yes")
  else:
    print("No")
  
  t -= 1
