N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())

drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌,우 
r, c = r-1, c-1
length = grid[r][c]

def in_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < N

# 폭탄 터트리기
for dr, dc in zip(drs, dcs):
    for l in range(length):
        nr, nc = r + dr * l, c + dc * l
        if in_range(nr, nc):
            grid[nr][nc] = 0

# 아래로 떨어지기
for r in range(N-1, 0, -1):
    for c in range(N):
        if grid[r][c] != 0:
            continue
        nr = r
        while nr > 0:
            if grid[nr][c] != 0:
                break
            nr -= 1
        if nr != r:
            grid[r][c] = grid[nr][c]
            grid[nr][c] = 0
for n in range(N):
    print(*grid[n])        