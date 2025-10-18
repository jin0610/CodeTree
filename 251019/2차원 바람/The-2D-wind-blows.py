N, M, Q = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

winds = [
    (int(r1) - 1, int(c1) - 1, int(r2) - 1, int(c2) - 1)
    for r1, c1, r2, c2 in [list(map(int, input().split())) for _ in range(Q)]
]

drs, dcs = [1, 0, -1, 0], [0, 1, 0, -1]     # D, R, U, L

# 범위내에 있는지 확인
def in_range(r, c, min_r, min_c, max_r, max_c):
    return r >= min_r and r <= max_r and c >= min_c and c <= max_c

# 시계방향으로 이동하기
def shift(wind):
    r1, c1, r2, c2 = wind
    temp = grid[r1][c1]
    r, c = r1, c1 # 현재 row, col
    d = 0
    nr, nc = r + drs[d], c + dcs[d] # 다음 row, col
    while True:
        grid[r][c] = grid[nr][nc]
        r, c = nr, nc
        nr, nc = r + drs[d], c + dcs[d]
        if not in_range(nr, nc, r1, c1, r2, c2):
            d = (d + 1) % 4
            nr, nc = r + drs[d], c + dcs[d]
        if nr == r1 and nc == c1:
            break
    grid[r1][c1 + 1] = temp

def mean_grid(wind):
    global grid
    temp = [    # 임시저장 grid 만들기
        grid[n][:]
        for n in range(N)
    ]
    r1, c1, r2, c2 = wind
    
    # 임시 grid에 평균값 넣기
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            num, cnt = grid[r][c], 1
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if in_range(nr, nc, 0, 0, N - 1, M - 1):
                    cnt += 1
                    num = num + grid[nr][nc]
            temp[r][c] = num // cnt
    grid = [    # 임시저장 grid 만들기
        temp[n][:]
        for n in range(N)
    ]

for q in range(Q):
    wind = winds[q]
    shift(wind)
    mean_grid(wind)

# 출력하기
for r in range(N):
    print(*grid[r])