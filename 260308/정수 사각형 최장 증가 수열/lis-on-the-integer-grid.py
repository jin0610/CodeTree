n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def count_dot(x, y):
    global dp, grid

    if dp[y][x] != 0:
        return dp[y][x]

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[ny][nx] > grid[y][x]:
            cnt = 1 + count_dot(nx,ny)    
    dp[y][x] = cnt + 1

    return cnt

# dp에 숫자가 저장되어 있지 않은 경우 숫자 세기 시작
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            count_dot(j, i)

answer = 0
for i in range(n):
    answer = max(answer, max(dp[i]))

print(answer)