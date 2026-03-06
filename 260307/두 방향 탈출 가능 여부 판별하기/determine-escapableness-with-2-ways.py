n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 1], [1, 0]


def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

def can_go(x, y):
    if in_range(x, y) and grid[y][x] == 1 and not visited[y][x] :
        return True
    return False

def dfs(x, y):
    global visited, dxs, dys

    for i in range(2):
        nx, ny = x + dxs[i], y + dys[i]
        if can_go(nx, ny):
            visited[ny][nx] = True
            dfs(nx, ny)

visited[0][0] = 1
dfs(0, 0)
print(int(visited[n-1][m-1]))
