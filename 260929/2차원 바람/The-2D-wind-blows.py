n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 시계방향 이동
def shift(r1, c1, r2, c2):

    # 우, 하, 좌, 상
    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

    temp = grid[r1][c1]
    curr_r, curr_c = r1, c1
    idx = 1
    while True:
        next_r, next_c = curr_r + drs[idx], curr_c + dcs[idx]
        if next_r < r1 or next_r > r2 or next_c < c1 or next_c > c2:
            idx = (idx - 1) % 4
            next_r, next_c = curr_r + drs[idx], curr_c + dcs[idx]

        if next_r == r1 and next_c == c1:
            break

        grid[curr_r][curr_c] = grid[next_r][next_c]
        curr_r, curr_c = next_r, next_c     
    grid[r1][c1 + 1] = temp

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

# 평균값으로 변경
def change_average_value(r1, c1, r2, c2):
    temp_grid = []
    for row in grid:
        temp_grid.append(row.copy())

    # 인접한 값(상, 하, 좌, 우)
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            values = [grid[r][c]]
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if in_range(nr, nc):
                    values.append(grid[nr][nc])
            temp_grid[r][c] = sum(values) // len(values)

    for r in range(r1, r2 + 1):
        grid[r] = temp_grid[r]


def simulation(r1, c1, r2, c2):
    # 시계방향 이동
    shift(r1, c1, r2, c2)

    # 평균값 변경
    change_average_value(r1, c1, r2, c2)


for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    simulation(r1, c1, r2, c2)

for i in range(n):
    print(*grid[i])