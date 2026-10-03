n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]
r, c = map(int, input().split())

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb(x, y):
    bomb_range = grid[x][y]

    # 1. 폭발
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    grid[x][y] = 0
    for dist in range(1, bomb_range):
        for dx, dy in zip(dxs, dys):
            cx, cy = x + dx * dist, y + dy * dist
            if in_range(cx, cy):
                grid[cx][cy] = 0

    # 2. 중력 적용
    for col in range(n):
        temp_row = n - 1
        for row in range(n - 1, -1, -1):
            if grid[row][col] != 0:
                if temp_row != row:
                    grid[temp_row][col] = grid[row][col]
                    grid[row][col] = 0

                temp_row -= 1

bomb(r - 1, c - 1)

for i in range(n):
    print(*grid[i])