n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]
r, c = map(int, input().split())

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb(x, y):
    bomb_range = grid[x][y]

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(bomb_range):
        if i == 0:
            grid[x][y] = 0
        else:
            for dx, dy in zip(dxs, dys):
                cx, cy = x + dx * i, y + dy * i

                if in_range(cx, cy):
                    grid[cx][cy] = 0

    for col in range(n):
        temp_row = n - 1
        start_sorting = False
        for row in range(n - 1, -1, -1):
            if not start_sorting and grid[row][col] == 0:
                start_sorting = True
                temp_row = row
                continue
            
            if start_sorting and grid[row][col] != 0:
                grid[temp_row][col] = grid[row][col]
                grid[row][col] = 0
                temp_row -= 1

bomb(r - 1, c - 1)

for i in range(n):
    print(*grid[i])
                



    
