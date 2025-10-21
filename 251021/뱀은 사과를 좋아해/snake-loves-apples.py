from collections import deque
N, M, K = map(int,input().split())

grid = [
    [0 for _ in range(N)]
    for _ in range(N)
]

# 사과 위치
for _ in range(M):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    grid[x][y] = 1

# 뱀의 움직임
snake_movement = [
    (direction, int(dist)) for direction, dist in [input().split() for _ in range(K)]
]

# 상 하 좌 우
dxs, dys = [-1, 1, 0, 0],[0, 0, -1, 1]
dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

snake = deque([(0, 0)])
length = 1
time = 0
for direction, dist in snake_movement:
    finished = False
    for d in range(1, dist + 1):
        time += 1
        cx, cy = snake[-1]
        nx, ny = cx + dirs[direction][0], cy + dirs[direction][1]
        if in_range(nx, ny) and (nx, ny) not in snake:   # 머리가 움직일 곳이 범위 내거나, 부딪히지 않았을 경우
            if grid[nx][ny] == 1:   # 사과가 있을 경우, 길이 + 1, deque 저장
                length += 1
                grid[nx][ny] = 0
            else:
                snake.popleft()
            snake.append((nx, ny))
        else:
            finished = True
            break
        
    if finished:
        break
            
print(time)