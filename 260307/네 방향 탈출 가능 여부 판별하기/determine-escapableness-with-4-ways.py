from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

visited = [[False for _ in range(m)] for _ in range(n)]


def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

def can_go(x, y):
    return in_range(x, y) and graph[y][x] == 1 and not visited[y][x]

def bfs():
    global q, dxs, dys

    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[ny][nx] = True

q = deque([(0, 0)])
visited[0][0] = True
bfs()
print(int(visited[n - 1][m - 1]))