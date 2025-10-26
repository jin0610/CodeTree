import sys
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    else:
        if not visited[x][y] and grid[x][y] == 1:
            return True
        else:
            return False

order = 1
def dfs(x, y):
    global order, visited

    visited[x][y] = True
    grid[x][y] = order
    order += 1

    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            dfs(nx, ny)

dfs(0, 0)
if visited[n-1][m-1]:
    print(1)
else:
    print(0)