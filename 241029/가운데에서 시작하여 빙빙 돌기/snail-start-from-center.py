n = int(input())
arr =[[0 for _ in range(n)] for __ in range(n)]

# 왼쪽, 위, 오른쪽 아래
dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

def in_range(r,c):
    return r >= 0 and r < n and c >= 0 and c < n

r = c = n-1
arr[r][c] = n * n
idx = 0

for i in range(n * n -1, 0, -1):
    nr, nc = r + dr[idx], c + dc[idx]
    if in_range(nr, nc) and arr[nr][nc] == 0:
        r, c = nr, nc
    else:
        idx = (idx + 1) % 4
        r, c = r + dr[idx], c + dc[idx]
    arr[r][c] = i

for i in range(n):
    print(*arr[i])