n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

drs, dcs = [-1, 1, 0,0], [0,0,-1,1]   # 상, 하, 좌, 우

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

# 십자 모양
def cross_shape_bomb(r, c, num):
    for dr, dc in zip(drs, dcs):
        for i in range(num):
            nr, nc = r + (dr * i), c + (dc * i)
            if in_range(nr, nc):
                grid[nr][nc] = 0

# 폭탄 
def bomb(col):
    for i in range(n):
        if grid[i][col] != 0:
            cross_shape_bomb(i, col, grid[i][col])
            break
        else:
            pass

# 중력 작동
def gravity():
    for i in range(n):
        for j in range(n - 1, 0, -1):
            if grid[j][i] == 0:
                grid[j][i] = grid[j - 1][i]
                grid[j - 1][i] = 0

for command in commands:
    bomb(command - 1)
    gravity()

# 출력하기
for i in range(n):
    print(*grid[i])