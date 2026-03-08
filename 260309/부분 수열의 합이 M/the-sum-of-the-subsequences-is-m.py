n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

# Please write your code here.

A = sorted(A)
_max = 10001
dp = [_max for _ in range(m + 1)]

dp[0] =0
print(A)
for i in range(1, n + 1):   # 원소들
    for j in range(m, -1, -1): # 목표 수
        if j >= A[i]:
            if dp[j - A[i]] == _max:
                continue
            dp[j] = min(dp[j], dp[j-A[i]] + 1)

if dp[-1] == _max:
    print(-1)
else:
    print(dp[-1])