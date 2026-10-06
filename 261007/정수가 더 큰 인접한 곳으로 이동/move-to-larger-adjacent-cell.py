n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited_grid = [[False] * n for _ in range(n)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n 

cx, cy = r - 1, c - 1
visited = [grid[cx][cy]]
visited_grid[cx][cy] = True
while True:
    move = False

    for dx, dy in zip(dxs, dys):
        nx, ny = cx + dx, cy + dy
        if in_range(nx, ny) and not visited_grid[nx][ny] and grid[nx][ny] > grid[cx][cy]:
            move = True
            visited.append(grid[nx][ny])
            visited_grid[nx][ny] = True
            cx, cy = nx, ny
            break

    if not move:
        break


print(*visited)