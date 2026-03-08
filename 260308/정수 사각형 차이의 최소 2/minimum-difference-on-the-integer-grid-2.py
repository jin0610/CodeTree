n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[(101, 0) for _ in range(n)] for _ in range(n)]

dp[0][0] = (grid[0][0],grid[0][0])
for i in range(1, n):
    dp[i][0] = (min(dp[i - 1][0][0], grid[i][0]), max(dp[i-1][0][1],  grid[i][0]))
    dp[0][i] = (min(dp[0][i - 1][0], grid[0][i]), max(dp[0][i-1][1],  grid[0][i]))

for i in range(1, n):
    for j in range(1, n):
        dot1 = (min(dp[i-1][j][0],grid[i][j]), max(dp[i-1][j][1],grid[i][j]))
        diff1 =  dot1[1]- dot1[0]
        dot2 = (min(dp[i][j-1][0],grid[i][j]), max(dp[i][j-1][1],grid[i][j]))
        diff2 = dot2[1]- dot2[0] 
        if diff1 > diff2:
            dp[i][j] = dot2
        elif diff1 < diff2:
            dp[i][j] = dot1
        else:
            dp[i][j] = (min(dot1[0],dot2[0]),max(dot1[1],dot2[0]))
print(dp[n-1][n-1][1] - dp[n-1][n-1][0])
'''
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
            elif dot1_diff > dot2_diff:
                dp[i][j] = (dot2[0], dot2[1], dot2_diff)
            else:
                dp[i][j] = (min(dot1[0],dot2[0]), max(dot1[1], dot2[1]), dot2_diff)



print(dp[n-1][n-1][2])   '''   