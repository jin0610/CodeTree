from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = []

for _ in range(k):
    x, y = map(int, input().split())
    points.append((x - 1, y - 1))

# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and grid[x][y] == 0 and not visited[x][y]

visited = [[False for _ in range(n)] for _ in range(n)]
for p in points:
    visited[p[0]][p[1]] = True

cnt = len(points)
def bfs():
    global cnt
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    q = deque(points)

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1

answer = 0
bfs()
# for p in points:
#     x, y = p
#     x, y = x - 1, y - 1
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     answer += bfs(x, y)

print(cnt)