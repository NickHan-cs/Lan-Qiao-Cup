import math

def is_prime(num):
    if num == 2 or num == 3:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n = int(input())
cnt = 0
ans = 1
i = 2
while cnt < n:
    if is_prime(i):
        ans = ans * i % 50000
        cnt += 1
    i += 1
print(ans)
