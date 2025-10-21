import sys
N = int(input())
x, y = map(int, input().split())

grid = [
    list(input())
    for _ in range(N)
]

visited = {}

# R, D, L, U
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

# 오른쪽에 벽이 있는지 확인
def wall_on_the_right(curr_x, curr_y, curr_d):
    right_d = (curr_d + 1) % 4
    nx, ny = curr_x + dxs[right_d], curr_y + dys[right_d]
    if in_range(nx, ny) and grid[nx][ny] == '#':
        return True
    return False

time = 0
x, y = x - 1, y - 1
d = 1 
visited[(x, y, d)] = 1
while True:
    nx, ny = x + dxs[d], y + dys[d]

    ## Step1: 바라보고 있는 방향으로 이동이 불가능할 경우 반시계 방향 90도
    if in_range(nx, ny) and grid[nx][ny] == '#':
        cnt = 0
        while in_range(nx,ny) and grid[nx][ny] == '#':
            d = (d + 3) % 4
            nx, ny = x + dxs[d], y + dys[d]
            cnt += 1

            if cnt == 4:
                print(-1)
                sys.exit(0)
    
    ## Step2: 바라보고 있는 방향으로 이동이 가능한 경우
    # Case 1: 바로 앞이 격자 밖이라면 이동하여 탈출
    if not in_range(nx, ny):
        time += 1
        break

    # 방문한 곳을 또 방문하면 빠져나갈 수 없는 것으로 판단
    if (nx, ny, d) in visited.keys():
        time = -1
        break

    # Case 2: 그 방향으로 이동했다 가정했을 때 해당 방향 기준으로 오른쪽에 벽이 있다면 그 방향으로 한칸 이동
    x, y = nx, ny
    visited[(x, y, d)] = 1
    time += 1
    
    # 오른쪽 확인 
    # Case 3: 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 벽이 존재하지 않을 경우
    # 현재 방향으로 이동 후 시계방향으로 방향 틈 
    if not wall_on_the_right(x, y, d):
        while not wall_on_the_right(x, y, d):
            d = (d + 1) % 4
            x, y = x + dxs[d], y + dys[d]
            visited[(x, y, d)] = 1
            time += 1
    
print(time)
