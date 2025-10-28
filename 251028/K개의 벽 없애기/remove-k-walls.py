from collections import deque

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

start_x, start_y = map(int,input().split())
end_x, end_y = map(int,input().split())
start_x, start_y, end_x, end_y = start_x - 1, start_y - 1, end_x - 1, end_y - 1

# 걸리는 시간 
times = [[N ** 2 for _ in range(N)] for _ in range(N)]

# 벽의 위치 저장
walls = []
for x in range(N):
    for y in range(N):
        if grid[x][y] == 1:
            walls.append((x, y))

# 범위 내 인지 확인
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

# 갈 수 있는 곳인지 판단하는 함수
def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and removed_grid[x][y] == 0

# 방문 여부 grid, time grid 초기화
def visited_initialize():
    for x in range(N):
        for y in range(N):
            visited[x][y] = False
            times[x][y] = N ** 2

visited = [[False for _ in range(N)] for _ in range(N)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs():
    global visited, distance

    visited_initialize()
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    times[start_x][start_y] = 0

    while q:
        cx, cy = q.popleft()
        now_time = times[cx][cy]

        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                times[nx][ny] = min(times[nx][ny], now_time + 1)

# 벽을 제거한 grid
removed_grid = []
def removed_walls(removed):
    global removed_grid

    removed_grid = [grid[i][:] for i in range(N)]   # grid copy
    # remove_walls에 있는 벽은 제거
    for x, y in removed:
        removed_grid[x][y] = 0

remove_walls = []
is_visited = False
answer = N**2
def choose_remove_walls(start, cnt):
    global remove_walls, visited, answer, is_visited

    if cnt == K:
        removed_walls(remove_walls)
        bfs()
        if visited[end_x][end_y]:
            is_visited = True
            answer = min(answer, times[end_x][end_y])
        return

    for w in range(len(walls)):
        remove_walls.append(walls[w])
        choose_remove_walls(w + 1, cnt + 1)
        remove_walls.pop()

    return
    
choose_remove_walls(0, 0)
if is_visited:
    print(answer)
else:
    print(-1)
