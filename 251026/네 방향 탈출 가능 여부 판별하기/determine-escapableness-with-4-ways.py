from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

# 범위 내 있는지 확인하는 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 움직일 수 있는지 확인
def can_go(x, y):
    if not in_range(x, y):
        return False

    if not visited[x][y] and grid[x][y] == 1:
        return True

    return False

# bfs
def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    q = deque([(0, 0)])

    while q:
        cx, cy = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)
