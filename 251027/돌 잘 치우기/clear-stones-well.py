from collections import deque
n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
grid2 = [[0 for _ in range(n)] for _ in range(n)]

# 시작점 저장
start_points = []
for _ in range(k):
    r, c = map(int,input().split())
    start_points.append((r - 1, c - 1))

# 방문여부 확인
visited = [[False for _ in range(n)] for _ in range(n)]

# 돌 위치 저장
stones = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            stones.append((r, c))

# 방문여부 초기화
def visited_intialize():
    for r in range(n):
        for c in range(n):
            if (r, c) in start_points:
                visited[r][c] = True
            else:
                visited[r][c] = False

# 범위 확인
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 갈 수 있는 곳인지 확인
def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid2[r][c] == 0

def bfs():
    global start_points, visited

    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited_intialize()
    
    q = deque(start_points) 
    size = k
    while q:
        cr, cc = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = cr + dr, cc + dc
            if can_go(nr, nc):
                q.append((nr, nc))
                visited[nr][nc] = True
                size += 1

    return size      

def update_grid(removed):
    global grid2
    grid2 = [grid[i][:] for i in range(n)]

    for r, c in removed:
        grid2[r][c] = 0
    
# 돌 두개 제거하는 backtraking
answer = 0
selected_stone = []
def remove_stones(start, cnt):
    global answer, selected_stone

    if cnt == m:
        update_grid(selected_stone)
        answer = max(answer, bfs())
        return

    for s in range(start, len(stones)):
        selected_stone.append(stones[s])
        remove_stones(s + 1, cnt + 1)
        selected_stone.pop()

    return

remove_stones(0, 0)
print(answer)