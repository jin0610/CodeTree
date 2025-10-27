from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
step = [[ n * m + 1 for _ in range(m)] for _ in range(n)]    # 거리를 적어두기 위한 grid
visited = [[False for _ in range(m)] for _ in range(n)]

# 범위 내인지 확인하는 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 갈 수 있는지 확인하는 함수
def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def bfs():
    global visited, step

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(0, 0)])
    visited[0][0] = True
    step[0][0] = 0

    while q:
        cx, cy = q.popleft()
        length = step[cx][cy]
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                step[nx][ny] = min(step[nx][ny],length + 1)
bfs()
if visited[n-1][m-1]:
    print(step[n-1][m-1])
else:
    print(-1)
