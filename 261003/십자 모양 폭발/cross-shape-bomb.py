n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def get_sorted():
    temp_grid = list(zip(*grid))

    for i in range(n):
        temp = []
        for num in temp_grid[i]:
            if num != 0:
                temp.append(num)

        if len(temp) != n:
            temp = (n - len(temp)) * [0] + temp

        temp_grid[i] = temp

    return list(zip(*temp_grid))


def bomb(r, c, grid):
    bomb_range = grid[r][c]
    drs, dcs = [-1, 1, 0, 0], [0, 0, 1, -1]

    for l in range(bomb_range):
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr * l, c + dc * l
            if in_range(nr, nc):
                grid[nr][nc] = 0
    
    grid = get_sorted()

    return grid

grid = bomb(r, c, grid)
        
for i in range(n):
    print(*grid[i])