N, M, K = map(int, input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

# 연속된 부분의 끝점 확인
def get_bomb_end_idx(curr_row, col, num):
    global grid
    for row in range(curr_row + 1, N):
        if grid[row][col] != num:
            return row - 1
    return N - 1

# 폭발
def bomb():
    while True:
        did_explode = False

        for c in range(N):
            for curr_row in range(N):
                if grid[curr_row][c] == 0:
                    continue
                
                end_row = get_bomb_end_idx(curr_row, c, grid[curr_row][c])
                if end_row - curr_row + 1 >= M:
                    for row in range(curr_row, end_row + 1):
                        grid[row][c] = 0
                    did_explode = True
        gravity()
        if not did_explode:
            return
        
# 회전
def rotation():
    global grid
    temp = [grid[r][:] for r in range(N)]

    for r in range(N):
        for c in range(N):
            grid[c][N - r - 1] = temp[r][c]

    gravity()

# 중력
def gravity():
    global grid
    for c in range(N):
        for r in range(N - 1, 0, -1):
            if grid[r][c] == 0:
                nr = r - 1
                while nr >= 0:
                    if grid[nr][c] != 0:
                        grid[r][c] = grid[nr][c]
                        grid[nr][c] = 0
                        break
                    else:
                        nr -= 1

for _ in range(K):
    bomb()
    rotation()
bomb()

cnt = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            cnt += 1
print(cnt)

