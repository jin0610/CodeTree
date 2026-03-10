n, m = map(int, input().split())    # n층, m개의 방
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(m)] for _ in range(n)]

# 초기화
for i in range(n):
    dp[0][i] = a[0][i]

for i in range(1, n):
    for j in range(m):
        for k in range(m):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + a[i][j])

answer = 0
for i in range(n):
    answer = max(answer, max(dp[i]))

print(answer)
