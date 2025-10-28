from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

step = [[n ** 2 for _ in range(n)] for _ in range(n)]

# 0 : 아무것도 없음, 1 : 귤, 2 : 상한 귤
# 범위 내인지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 갈 수 있는 곳인지 확인
def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

# 상한 귤 위치
rotten = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            rotten.append((x, y))

visited = [[False for _ in range(n)] for _ in range(n)]

def bfs():
    global visited, answer, rotten

    q = deque(rotten)
    for rx, ry in rotten:
        visited[rx][ry] = True
        step[rx][ry] = 0

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        cx, cy = q.popleft()
        time = step[cx][cy]
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True

                step[nx][ny] = min(step[nx][ny], time + 1)

bfs()
answer = [[-1 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            if grid[x][y] == 0:
                step[x][y] = -1
            if step[x][y] == n ** 2:
                step[x][y] = -2

for i in range(n):
    print(*step[i])