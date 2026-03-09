n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
dp = [[0 for _ in range(5)] for _ in range(n + 1)]

# 초기화
dp[1][1] = coin[1]
if n > 1:
    dp[2][0] = coin[2]
    dp[2][2] = coin[1] + coin[2]


for i in range(3, n + 1):
    for j in range(4):
        if dp[i-2][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i])
        if j and dp[i - 1][j - 1] != 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin[i])

# 가능한 모든 경우에서 최대 가치를 찾아 출력합니다.
ans = max(dp[n])
print(ans)