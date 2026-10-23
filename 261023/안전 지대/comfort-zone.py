import sys
sys.setrecursionlimit(10_000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * m for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    if not in_range(x, y):
        return False

    if not visited[x][y] and grid[x][y] > k:
        return True

    return False

def find_safe_area(x, y, k):
    global visited, grid

    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            find_safe_area(nx, ny, k)

k = 1
safe_areas = []
while True:
    visited = [[False] * m for _ in range(n)]
    count_of_safe_area = 0

    for x in range(n):
        for y in range(m):
            if can_go(x, y, k):
                find_safe_area(x, y, k)
                count_of_safe_area += 1

    safe_areas.append(count_of_safe_area)

    if count_of_safe_area == 0:
        break

    k += 1

max_count_of_area = max(safe_areas)
max_height = safe_areas.index(max_count_of_area) + 1
print(max_height, max_count_of_area)