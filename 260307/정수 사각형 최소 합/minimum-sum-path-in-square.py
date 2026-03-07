n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n - 1, -1, -1):
        if i == 0 and j == n:
            dp[i][j] = grid[i][j]
        elif j == n - 1:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j+1] + grid[i][j]
        else:
            dp[i][j] = min(dp[i][j+1], dp[i-1][j]) + grid[i][j]

print(dp[n-1][0])
