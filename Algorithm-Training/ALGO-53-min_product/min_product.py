t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = list(map(int, input().split()))
    b.sort()
    ans = 0
    for j in range(n):
        ans += a[j] * b[j]
    print(ans)
