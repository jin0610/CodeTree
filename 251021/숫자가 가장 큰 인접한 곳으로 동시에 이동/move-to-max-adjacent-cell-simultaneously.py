N, M, T = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 구슬의 위치
marbles = [
    (r - 1, c - 1) for r, c in [map(int, input().split()) for _ in range(M)]
]

# 상, 하, 좌, 우
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
def in_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < N

def get_beads_new_position():    
    global grid, marbles
    new_position = []
    for beads in marbles:
        r, c = beads
        max_r, max_c, max_num = r, c, grid[r][c]
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc):
                if grid[nr][nc] > max_num:
                    max_num = grid[nr][nc]
                    max_r, max_c = nr, nc

        if (max_r, max_c) not in new_position:
            new_position.append((max_r, max_c))
        else:
            new_position.remove((max_r, max_c))
    
    marbles = new_position
    return marbles

for _ in range(T):
    get_beads_new_position()

print(len(marbles))