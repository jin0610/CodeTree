from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[False] * m for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and a[x][y] == 1

def bfs(x, y):

    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True

bfs(0, 0)
print(int(visited[n - 1][m - 1]))

