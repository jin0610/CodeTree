n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r, c = r - 1, c - 1



def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def shift(r, c, w, h, dir):
    if dir == 0:
        # 반시계방향(1 -> 2 -> 3 -> 4) w -> h
        dxs, dys, moves = [-1, -1, 1, 1], [1, -1, -1, 1], [w, h, w, h]
    else: 
        # 시계방향() h -> w
        dxs, dys, moves = [-1, -1, 1, 1], [-1, 1, 1, -1], [h, w, h, w]

    points = []
    values = []
    curr_r, curr_c = r, c
    for dx, dy, m in zip(dxs, dys, moves):
       for _ in range(m):
        curr_r, curr_c = curr_r + dx, curr_c + dy
        points.append((curr_r, curr_c))
        values.append(grid[curr_r][curr_c])

    temp = values.pop()
    values.insert(0, temp)

    for i in range(len(points)):
        x, y = points[i]
        grid[x][y] = values[i]

shift(r, c, m1, m2, dir)

for i in range(n):
    print(*grid[i])