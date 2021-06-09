spaces = 4
i = 1

while i <= 18:
    print(" " * spaces + "*" * i)
    if spaces > 0:
         spaces -= 1
    else:
        break
    i += 2
