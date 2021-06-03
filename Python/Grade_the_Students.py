n = int(input())

for i in range(n):
  maths, algo = [int(i) for i in input().split()]
  if maths > 70 and algo > 50:
    print("Pass")
  else:
    print("Fail")
