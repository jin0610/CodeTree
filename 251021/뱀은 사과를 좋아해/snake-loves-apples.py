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
time = 0
move_idx = 0
while move_idx < K:
    finished = False
    direction, dist = snake_movement[move_idx]

    for _ in range(dist):
        time += 1
        cx, cy = snake[-1]
        nx, ny = cx + dirs[direction][0], cy + dirs[direction][1]
        # 범위내에 있는 지 판단
        if not in_range(nx, ny):
            finished = True
            break

        # 사과가 있을 경우 사과를 먹고 길이 늘림
        if grid[nx][ny] == 1:
            grid[nx][ny] = 0
        else: 
            x, y = snake.popleft()

        # 머리가 다음으로 이동할 nx,ny칸에 꼬리가 있을 경우 break
        if (nx, ny) in snake:
            finished = True
            break 
        snake.append((nx, ny))
        
    if finished:
        break

    move_idx += 1
            
print(time)