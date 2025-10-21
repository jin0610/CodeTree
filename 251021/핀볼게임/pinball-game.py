n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# R, D, L, U
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def get_time(x, y, d):
    time = 1
    while True:
        time += 1

        # 방향 정리
        if grid[x][y] == 1:
            if d % 2 == 0:
                d = (d + 3) % 4
            else:
                d = (d + 1) % 4
        elif grid[x][y] == 2:
            if d % 2 == 0:
                d = (d + 1) % 4
            else:
                d = (d + 3) % 4

        nx, ny = x + dxs[d], y + dys[d] # 다음 이동할 칸
        if not in_range(nx, ny):
            break
        x, y = nx, ny   # 이동
        

    return time

max_time = 0
# 우측으로 들어오는 경우
for i in range(n):
    max_time = max(max_time, get_time(i, 0, 0)) # 우측으로 들어가는 경우
    max_time = max(max_time, get_time(0, i, 1)) # 아래쪽에서 들어가는 경우
    max_time = max(max_time, get_time(i, n - 1, 2)) # 왼쪽으로 들어가는 경우
    max_time = max(max_time, get_time(n - 1, i, 3)) # 위쪽으로 들어가는 경우

print(max_time)