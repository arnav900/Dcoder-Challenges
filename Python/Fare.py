f_km, for_f_km, per_km, distance = [int(i) for i in input().split()]

if distance > f_km:
  print((distance - f_km) * per_km + for_f_km)
else:
  print(4)
