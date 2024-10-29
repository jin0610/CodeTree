n, m  = map(int, input().split())

arr = [[0 for i in range(m)] for _ in range(n)]

# 우 하 좌 상
dr, dc = [0, 1, 0, -1], [ 1, 0, -1, 0]
r, c = 0, 0
arr[r][c] = 1
idx = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for i in range(1, n * m):
    nr, nc = r + dr[idx], c + dc[idx]

    if in_range(nr, nc) :
        if arr[nr][nc] == 0:
            r, c = nr, nc
            
    else:
        idx = (idx + 1) % 4
        r, c = r + dr[idx], c +dc[idx]
    arr[r][c] = i + 1


for i in range(n):
    print(*arr[i])