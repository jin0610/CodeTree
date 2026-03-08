n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[(101, 0, 101) for _ in range(n)] for _ in range(n)] # (min, max, max-min)
dxs, dys = [0, 1], [1, 0]

answer = 0
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = (grid[i][j], grid[i][j], grid[i][j] - grid[i][j])
        elif i == 0:
            _min, _max = min(dp[i][j-1][0], grid[i][j]), max(dp[i][j-1][1], grid[i][j]) 
            _diff = _max - _min
            dp[i][j] = (_min, _max, _diff)
        elif j == 0:
            _min, _max = min(dp[i-1][j][0], grid[i][j]), max(dp[i-1][j][1], grid[i][j]) 
            _diff = _max - _min
            dp[i][j] = (_min, _max, _diff)
        else:
            dot1 = (min(dp[i-1][j][0], grid[i][j]), max(dp[i-1][j][1], grid[i][j]))
            dot1_diff = dot1[1]-dot1[0]
            dot2 = (min(dp[i][j-1][0], grid[i][j]), max(dp[i][j-1][1], grid[i][j]))
            dot2_diff = dot2[1]-dot2[0]

            if dot1_diff < dot2_diff:
                dp[i][j] = (dot1[0], dot1[1], dot1_diff)
            else:
                dp[i][j] = (dot2[0], dot2[1], dot2_diff)


print(dp[n-1][n-1][2])      