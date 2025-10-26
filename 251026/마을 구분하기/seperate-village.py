n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

# Please write your code here.
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    else:
        if not visited[x][y] and grid[x][y] == 1:
            return True
        else:
            return False


person = 0
def dfs(x, y):
    global visited, person
    visited[x][y] = True
    person += 1
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            dfs(nx, ny)
  
answer = 0
persons = []
for x in range(n):
    for y in range(n):
        person = 0
        if can_go(x, y):
            dfs(x, y)
            answer += 1
            persons.append(person)
print(answer)
persons = sorted(persons)
for p in persons:
    print(p)