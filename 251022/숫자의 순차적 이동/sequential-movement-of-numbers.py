n, m = map(int, input().split())
grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]

# 8방향
drs = [-1, -1, -1, 0, 1, 1, 1, 0]
dcs = [-1, 0, 1, 1, 1, 0, -1, -1]

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def move(r, c, num):
    global grid
    max_num, max_r, max_c = 0, 0, 0
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr,nc):
            if grid[nr][nc] > max_num:
                max_num = grid[nr][nc]
                max_r, max_c = nr, nc
    grid[r][c], grid[max_r][max_c] = grid[max_r][max_c], grid[r][c]

def all_move():
    global grid
    for num in range(1, n ** 2 + 1):
        for r in range(n):
            if num in grid[r]:
                c = grid[r].index(num)
                move(r, c, num)
                break

for _ in range(m):
    all_move()

for r in range(n):
    print(*grid[r])