n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for __ in range(n)]
char = [chr(ord('A') + i) for i in range(26)]
# 오른쪽 아래 왼 위
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(r,c):
    return r >= 0 and r < n and c >= 0 and c < m

r, c = 0, 0
arr[r][c] = 'A'
idx = 0

for i in range(1, n * m):
    nr, nc = r + dr[idx], c + dc[idx]
    if in_range(nr, nc) and arr[nr][nc] == 0:
        r, c = nr, nc
    else:
        idx = (idx + 1) % 4
        r, c = r + dr[idx], c + dc[idx]
    arr[r][c] = char[i % 26]
    

for i in range(n):
    print(*arr[i])