from collections import deque
import sys

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
visited = [[False for _ in range(n)] for _ in range(n)]
step = [[n ** 2 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return  0 <= x < n and 0 <= y < n

def bfs():
    global visited

    q = deque([(r1 - 1, c1 - 1)])
    visited[r1-1][c1-1] = True
    step[r1-1][c1-1] = 0
    
    while q:
        cx, cy = q.popleft()
        length = step[cx][cy]

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                step[nx][ny] = min(step[nx][ny], length + 1)

bfs()
if visited[r2 - 1][c2 - 1]:
    print(step[r2 - 1][c2 - 1])
else:
    print(-1)