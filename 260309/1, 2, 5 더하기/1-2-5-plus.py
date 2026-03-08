n = int(input())

# Please write your code here.
nums = [1, 2, 5]

dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    for num in nums:
        if i >= num:
            dp[i] += dp[i-num]

print(dp[-1] % 10007)