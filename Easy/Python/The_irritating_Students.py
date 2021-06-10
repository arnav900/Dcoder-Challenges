t = int(input())

while t:
  
  n = int(input())
  if n % 2 == 0:
    print(n // 2, n // 2)
  else:
    print(n // 2, (n // 2) + 1)
    
  t -= 1
