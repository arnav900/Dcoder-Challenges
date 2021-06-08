m1, m2, m3 = [int(i) for i in input().split()]

mean = (m1 + m2 + m3) / 3

if mean > 90 and mean <= 100:
  print('A')

elif mean > 80 and mean <= 90:
  print('B')

elif mean > 70 and mean <= 80:
  print('C')

elif mean > 60 and mean <= 70:
  print('D')

elif mean <= 60:
  print('F')

else:
  print("Invalid Character")
