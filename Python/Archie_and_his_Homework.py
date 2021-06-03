N, D = input().split()
N, D = int(N), int(D)
x, y = N, D
while y > 0:
  x = x % y
  y ^= x
  x ^= y
  y ^= x
print(int(N/x), int(D/x))
