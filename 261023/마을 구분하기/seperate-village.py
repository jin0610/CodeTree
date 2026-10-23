n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if not visited[x][y] and grid[x][y] == 1:
        return  True
    
    return False

count_of_person = 0
count_of_village = 0
def find_village(x, y):
    global grid, visited, count_of_person

    count_of_person += 1
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            
            find_village(nx, ny)

persons = []
for x in range(n):
    for y in range(n):
        count_of_person = 0
        if not visited[x][y] and grid[x][y] == 1:
            count_of_village += 1
            find_village(x, y)
            persons.append(count_of_person)

persons = sorted(persons)
print(count_of_village)
for i in range(count_of_village):
    print(persons[i])
