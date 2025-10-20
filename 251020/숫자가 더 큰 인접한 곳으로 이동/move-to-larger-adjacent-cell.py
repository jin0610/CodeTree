n, r, c = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

r, c = r - 1, c - 1
# 상, 하, 좌, 우
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

while True:
    print(grid[r][c], end =" ")

    is_bigger = False

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] > grid[r][c]:
            r, c = nr, nc
            is_bigger = True
            break
    
    if not is_bigger:
        break
         