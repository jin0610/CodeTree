n,m = map(int, input().split())
arr = [ [0 for _ in range(m)] for __ in range(n)]

# 아래 오른 위 왼
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

arr[0][0] = 1
r, c = 0, 0
idx = 0
for i in range(1, n*m):
    nr, nc = r + dr[idx], c + dc[idx]
    if in_range(nr, nc) and arr[nr][nc] == 0:
        r, c = nr, nc
        arr[r][c] = i + 1
    else:
        idx = (idx + 1) % 4
        r, c = r + dr[idx], c + dc[idx]
        arr[r][c] = i + 1
    
  
for i in range(n):
    print(*arr[i])