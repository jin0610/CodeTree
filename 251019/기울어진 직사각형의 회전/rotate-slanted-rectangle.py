n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, d = map(int, input().split())

r, c = r - 1, c - 1
drs, dcs = [-1, -1, 1, 1], [1, -1, -1, 1] # 1번, 2번, 3번, 4번
length = [m1, m2, m3, m4]


idx = 0
temp = grid[r][c]
if d == 1:
    cr, cc = r, c
    for dr, dc, l in zip(drs, dcs, length):
        for _ in range(l):
            nr, nc = cr + dr, cc + dc
            grid[cr][cc] = grid[nr][nc]
            cr, cc = nr, nc
    grid[r - 1][c - 1] = temp
else:
    cr, cc = r, c
    for dr, dc, l in reversed(list(zip(drs, dcs, length))):
        for i in range(l):
            nr, nc = cr - dr, cc - dc
            grid[cr][cc] = grid[nr][nc]
            cr, cc = nr, nc
    grid[r - 1][c + 1] = temp

for i in range(n):
    print(*grid[i])
