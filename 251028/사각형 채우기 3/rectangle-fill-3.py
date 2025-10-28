n = int(input())

dp = [0] * (n + 1)
dp[1] = 2
dp[2] = 7

# f(n) = f(n-1) * f(n-2)
for i in range(n+1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 1000000007)