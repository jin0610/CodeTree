n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

# 가장 큰 수 찾기
numbers = []
for x in range(n):
    for y in range(n):
        if grid[x][y] not in numbers:
            numbers.append(grid[x][y])

# 범위 내인지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 갈 수 있는 지 확인
def can_go(x, y, num):
    if not in_range(x, y):
        return False

    if not visited[x][y] and grid[x][y] == num:
        return True
    
    return False

def dfs(x, y, num):
    global visited, size

    size += 1
    visited[x][y] = True

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, num):
            dfs(nx, ny, num)

max_size = 0
bomb = 0
for num in numbers:
    for x in range(n):
        for y in range(n):
            size = 0
            if can_go(x, y, num):
                dfs(x, y, num)  
                max_size = max(max_size, size) 
                if size >= 4:
                    bomb += 1

print(bomb, max_size)
            


            