k, l = map(int, input().split())
dp = [[0 for j in range(l + 1)] for i in range(k)]
mod = 1000000007
for i in range(k):
    dp[i][1] = 1
for j in range(2, l + 1):
    for i in range(k):
        for t in range(k):
            if i != t + 1 and i != t - 1:
                dp[i][j] = (dp[i][j] + dp[t][j - 1]) % mod
ans = 0
for i in range(1, k):
    ans = (ans + dp[i][l]) % mod
print(ans)
