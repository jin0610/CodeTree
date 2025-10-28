from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
distance = [[n**2 for _ in range(n)] for _ in range(n)]

# 0 : 이동 가능, 1 : 벽, 2: 사람, 3 : 비를 피할 수 있는 곳
# 사람이 있는 곳 
persons = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            persons.append((x, y))

# 범위 내에 있는 지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 갈 수 있는 지 확인
def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 1

# visited 방문 여부 표시하는 grid 초기화
def visited_initalize():
    global visited
    for x in range(n):
        for y in range(n):
            visited[x][y] =  False
            distance[x][y] = n ** 2

dxs, dys = [-1, 1, 0, 0], [0,0, -1, 1]
def bfs(x, y):
    global visited, distance
    # 초기화
    visited_initalize()

    q = deque([(x, y)]) # q에 사람 위치 담기
    visited[x][y] = True  
    distance[x][y] = 0    # 거리 0

    while q:
        cx, cy = q.popleft()
        dist = distance[cx][cy]

        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = min(distance[nx][ny], dist + 1)
            
                if grid[nx][ny] == 3:
                    return distance[nx][ny]
    return -1
    
answer = [ [0 for _ in range(n)] for _ in range(n)] # 사람이 비를 피할 수 있다면 최소 시간
for x, y in persons:
    answer[x][y] = bfs(x, y)

for x in range(n):
    print(*answer[x])
