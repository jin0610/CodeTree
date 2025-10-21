N, M, r, c = map(int,input().split())
grid = [
    [0 for _ in range(N)]
    for _ in range(N)
]

r, c = r - 1, c - 1
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
def in_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < N

bomb_location = [(r, c)]
grid[r][c] = 1
for t in range(1, M + 1):
    length = 2 ** (t - 1)
    new_bomb=[]
    for cr, cc in bomb_location:
        for dr, dc in zip(drs, dcs):
            nr, nc = cr + (dr * length), cc + (dc * length)
            if in_range(nr, nc):
                grid[nr][nc] = 1
                if (nr, nc) not in bomb_location:
                    new_bomb.append((nr, nc))
    bomb_location += new_bomb

bomb_cnt = 0
for i in range(N):
    bomb_cnt += sum(grid[i])
print(bomb_cnt)