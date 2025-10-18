N, M, Q = map(int, input().split())
grid = [
    list(map(int, input().split())) 
    for _ in range(N)
]
winds = [
    (int(r)-1, d) 
    for r, d in [input().split() for _ in range(Q)]
]

# 움직이기
def shift(row, d):
    if d == "L" or d == 1: # 왼쪽은 1, L
        temp = grid[row][M - 1]
        for i in range(M - 1, 0, -1):
            grid[row][i] = grid[row][i - 1]
        grid[row][0] = temp
    else:   # 오른쪽은 0, R
        temp = grid[row][0]
        for i in range(M - 1):
            grid[row][i] = grid[row][i + 1]
        grid[row][M - 1] = temp

# 전파 여부 확인
def isSpread(row1, row2):
    for m in range(M):
        if grid[row1][m] == grid[row2][m]:
            return True
    return False

for q in range(Q):
    row, direction = winds[q]
    shift(row, direction)
    # 위방향
    if direction == "L": d = 1
    else: d = 0
    for r in range(row, 0, -1):
        if isSpread(r, r - 1):
            d += 1
            shift(r - 1, d % 2)
        else:
            break
            
    # 아래방향
    if direction == "L": d = 1
    else: d = 0
    for r in range(row, N - 1):
        if isSpread(r, r + 1):
            d = d + 1
            shift(r + 1, d % 2)
        else:
            break

# 출력하기
for n in range(N):
    print(*grid[n])