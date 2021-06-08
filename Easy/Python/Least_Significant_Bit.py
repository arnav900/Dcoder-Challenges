t = int(input())

while t:
  
  num = int(input())
  bin_num = bin(num).replace('0b', '')
  if bin_num[-1] == '1':
    print("Yes")
  else:
    print("No")
  
  t -= 1
