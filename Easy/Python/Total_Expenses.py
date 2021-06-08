t = int(input())

while t:
  
  price = int(input())
  
  if price > 1000:
    discount = (10 / 100) * price
    price -= discount
  
  print("%.2f"%price)
  
  t -= 1
