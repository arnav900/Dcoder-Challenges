from math import sqrt, pow

home = (0, 0)
arr = [int(i) for i in input().split()]
truckA = (arr[0], arr[1])
truckB = (arr[2], arr[3])

distanceA = sqrt(pow(truckA[0] - home[0], 2) + pow(truckA[1] - home[1], 2))
distanceB = sqrt(pow(truckB[0] - home[0], 2) + pow(truckB[1] - home[1], 2))

if distanceA < distanceB:
  print("A")
else:
  print("B")
