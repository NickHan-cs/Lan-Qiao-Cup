n = int(input())
if n == 1 or n == 2:
    print(1)
else:
    a, b, ans = 1, 1, 0
    for i in range(2, n):
        ans = (a + b) % 10007
        a, b = b, ans
    print(ans)
