l, r = map(int, input().split())
ans = 0
for i in range(l, r+1):
    num = bin(i)
    for j in range(2, len(num)):
        if num[j] == '1':
            ans += 1
print(ans)
