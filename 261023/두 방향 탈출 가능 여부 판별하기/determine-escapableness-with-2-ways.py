n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 1], [1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m
def can_go(x,y):
    if not in_range(x, y):
        return False
    
    if grid[x][y] == 1 and not visited[x][y]:
        return True
    
    return False

def dfs(x, y):
    global grid, visited, escaped

    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            # visited[nx][ny] = True
            dfs(nx,ny)

# visited[0][0] = True
dfs(0, 0)
print(int(visited[n - 1][m - 1]))

