n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y <  n

def can_go(x, y):
    return in_range(x, y) and grid[y][x] == 1 and not visited[y][x]

def dfs(x, y):
    global visited, dxs, dys, people_cnt

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[ny][nx] = True
            people_cnt += 1
            dfs(nx, ny)

town = 0
people = []
for i in range(n):
    for j in range(n):
        if can_go(j, i):
            visited[i][j] = True
            town += 1
            people_cnt = 1
            dfs(j, i)
            people.append(people_cnt)

print(town)
people = sorted(people)
for i in range(len(people)):
    print(people[i])

