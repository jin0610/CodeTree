from collections import deque
N, K, U, D = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, height):
    return in_range(x, y) and not visited[x][y] and U <= abs(height - grid[x][y]) <= D

def visited_initalize():
    for x in range(N):
        for y in range(N):
            visited[x][y] = False

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(cities):
    global visited
    visited_initalize()

    q = deque(cities)
    for x, y in cities:
        visited[x][y] = True

    cnt = K
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny, grid[cx][cy]):
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1


    return cnt

cities = []
answer = 0
def select_city(start, cnt):
    global cities, answer

    if cnt == K:
        answer = max(answer, bfs(cities))
        return

    for s in range(start, N * 2 - 1):
        cities.append((s // N, s % N))
        select_city(s + 1, cnt + 1)
        cities.pop()

    return

select_city(0, 0)
print(answer)