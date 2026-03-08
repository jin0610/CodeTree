N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
dp = [10001 for _ in range(M + 1)]

for value in coin:
    dp[value] = 1

for i in range(1, M + 1):
    for j in range(N):
        if i - coin[j] >= 0:
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])