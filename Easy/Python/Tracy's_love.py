num1, num2 = [int(i) for i in input().split()]

if num1 + num2 == 6 or abs(num1 - num2) == 6:
  print("Love")
else:
  print("Hate")
