n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bomb(r, c, bomb_range):
    drs, dcs = [-1, 1, 0, 0], [0, 0, 1, -1]

    # 1. 폭발
    for dist in range(bomb_range):
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr * dist, c + dc * dist 
            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                grid[nr][nc] = 0

    # 2. 중력
    
    for col in range(n):
        temp = None
        for row in range(n - 1, -1, -1):
            if temp is None and grid[row][col] == 0:
                temp = row
            
            if temp is not None and grid[row][col] != 0:
                grid[temp][col] = grid[row][col]
                grid[row][col] = 0
                temp -= 1

for _ in range(m):
    bomb_col = int(input())
    bomb_col -= 1
    
    for row in range(n):
        if grid[row][bomb_col] != 0:
            bomb_range = grid[row][bomb_col]
            bomb(row, bomb_col, bomb_range)
            break


for i in range(n):
    print(*grid[i])