n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
_max = 10001
dp = [_max for _ in range(m + 1)]
dp[0] = 0

for i in range(n):
    for j in range(m, -1, -1):
        if j - A[i] >= 0:
            dp[j] = min(dp[j], dp[j - A[i]] + 1)

if dp[-1] == _max:
    print(-1)
else:
    print(dp[-1])
