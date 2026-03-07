n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        elif i == 0:
            dp[i][j] = min(grid[i][j], dp[i][j - 1])
        elif j == 0:
            dp[i][j] = min(grid[i][j], dp[i - 1][j])
        else:
            dp[i][j] = max(min(grid[i][j], dp[i][j - 1]), min(grid[i][j], dp[i - 1][j]))

print(dp[n-1][n-1])
