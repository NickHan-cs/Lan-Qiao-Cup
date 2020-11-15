def FindRoot(x, h):
    if f[x] == x:
        return (x, h)
    return FindRoot(f[x], h+1)


m, n = map(int, input().split())
k = int(input())
f = [i for i in range(m*n+1)]
for i in range(k):
    a, b = map(int, input().split())
    a_fa, a_h = FindRoot(a, 0)
    b_fa, b_h = FindRoot(b, 0)
    if a_h < b_h:
        f[a_fa] = b_fa
        f[a] = b_fa
        f[b] = b_fa
    else:
        f[b_fa] = a_fa
        f[b] = a_fa
        f[a] = a_fa
f_set = set()
ans = 0
for i in range(1, m*n+1):
    f[i] = FindRoot(i, 0)[0]
    if f[i] not in f_set:
       ans += 1
       f_set.add(f[i])
print(ans)
