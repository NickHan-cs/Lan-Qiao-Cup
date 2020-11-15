import math

n = int(input())
if n <= 0:
    print(0)
else:
    n_sqrt = int(math.sqrt(n))
    if n_sqrt ** 2 == n:
        print(n)
    else:
        print((n_sqrt + 1) ** 2)