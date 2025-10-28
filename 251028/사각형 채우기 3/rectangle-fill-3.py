n = int(input())
dp = [0] * (n + 3)
dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(4, n+1):
    dp[i] = dp[i - 1] * dp[i - 2] + 2** i

print(dp[n])
