def find(x):
    global h
    if f[x] == x:
        return x
    else:
        h += 1
        return find(f[x])

n, p = map(int, input().split())
c = []
for i in range(n):
    c.append(int(input()))
r = []
for i in range(p):
    s, e, l = map(int, input().split())
    l = 2 * l + c[s-1] + c[e-1]
    r.append((s, e, l))
f = [0 for i in range(n+1)]
for i in range(1, n+1):
    f[i] = i
r.sort(key=lambda x: x[2])
num = 0
ans = 0
for r_i in r:
    h = 0
    a = find(r_i[0])
    a_h = h
    h = 0
    b = find(r_i[1])
    b_h = h
    if a != b:
        ans += r_i[2]
        num += 1
        if a_h < b_h:
            f[a] = b
        else:
            f[b] = a
    f[r_i[0]] = f[a]
    f[r_i[1]] = f[b]
    if num == n:
        break
print(ans + min(c))
