n, m = list(map(int, input().split()))

arr = [[0] * m for _ in range(n)]

# 범위 내인지 확인
def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

# 시계방향 (row, col) 우 하 좌 상
drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

# 초기설정
dir_idx = 0
arr[0][0] = 1
r, c = 0, 0
for i in range(2, n * m + 1):
    nr, nc = r + drs[dir_idx], c + dcs[dir_idx]

    if in_range(nc, nr) and arr[nr][nc] == 0:
        r, c = nr, nc
        
    else:
        dir_idx = (dir_idx + 1) % 4
        r, c = r + drs[dir_idx], c + dcs[dir_idx]
    arr[r][c] = i

for i in range(n):
    print(*arr[i])