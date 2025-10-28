n = int(input())

dp = [0] * 1001
dp[2] = 1
dp[3] = 1
dp[4] = 1

for i in range(4, n + 1):
    if i % 5 == 0:
        dp[i] = dp[i - 5] + 2
    elif i % 5 == 2:
        dp[i] = dp[i - 2] + 1
    elif i % 5 == 3:
        dp[i] = dp[i - 3] + 1
    else:
        pass

print(dp[n] % 10007)
