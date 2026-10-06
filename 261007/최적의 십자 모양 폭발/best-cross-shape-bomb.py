n = int(input())
bomb_grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def check_grid(grid):
    cnt = 0

    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:
                continue

            for dr, dc in zip(drs, dcs):
                nr, nc = row + dr, col + dc
                if in_range(nr, nc) and grid[row][col] == grid[nr][nc]:
                    cnt += 1

    return cnt // 2

def bomb(grid, row, col, bomb_range):
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 1. 폭발
    for dist in range(bomb_range):
        for dr, dc in zip(drs, dcs):
            nr, nc = row + dr * dist, col + dc * dist
            if in_range(nr, nc):
                grid[nr][nc] = 0

    # 2. 중력
    for c in range(n):
        temp = None
        for r in range(n - 1, -1, -1):
            if temp is None and grid[r][c] == 0:
                temp = r
            if temp is not None and grid[r][c] != 0:
                grid[temp][c] = grid[r][c]
                grid[r][c] = 0
                temp -= 1

    return grid

def print_grid(grid):
    for i in range(n):
        print(*grid[i])
    print("=========================")

answer = 0
for row in range(n):
    for col in range(n):
        bomb_range = bomb_grid[row][col]

        temp_grid = [bomb_grid[i][:] for i in range(n)]

        temp_grid = bomb(temp_grid, row, col, bomb_range)

        cnt = check_grid(temp_grid)
        
        answer = max(answer, cnt)

print(answer)