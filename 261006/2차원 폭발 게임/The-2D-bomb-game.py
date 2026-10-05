n, m, k = map(int, input().split())
bomb_grid = [list(map(int, input().split())) for _ in range(n)]

def get_count_of_bomb(row, col, num):
    cnt = 1
    for curr_row in range(row + 1, n):
        if bomb_grid[curr_row][col] != bomb_grid[row][col]:
            return curr_row - 1, cnt
        else:
            cnt += 1
    return n - 1, cnt

# 폭발
def bomb(grid):
    for col in range(n):
        while True:
            did_exploded = False

            # 폭발
            row = 0
            while True:
                if row >= n:
                    break

                if grid[row][col] != 0:
                    end_row, cnt = get_count_of_bomb(row, col, grid[row][col])
                    if  cnt >= m:
                        for target in range(row, end_row + 1):
                            grid[target][col] = 0
                        did_exploded = True
                    row = end_row + 1
                else:
                    row += 1

            if not did_exploded:
                break

            temp = None
            for row in range(n - 1, -1, -1):
                if temp is None and grid[row][col] == 0:
                    temp = row
                
                if temp is not None and grid[row][col] != 0:
                    grid[temp][col] = grid[row][col]
                    grid[row][col] = 0
                    temp -= 1

    return grid

# 중력
def gravity(grid):
    for col in range(n):
        temp = None
        for row in range(n - 1, -1, -1):
            if temp is None and grid[row][col] == 0:
                temp = row
            
            if temp is not None and grid[row][col] != 0:
                grid[temp][col] = grid[row][col]
                grid[row][col] = 0
                temp -= 1
    return grid

# 회전
def rotation(grid):
    temp_grid = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if grid[row][col] != 0:
                temp_grid[col][n - row - 1] = grid[row][col]
    return temp_grid


for _ in range(k):
    # 1. 폭발
    bomb_grid = bomb(bomb_grid)

    # 3. 회전
    bomb_grid = rotation(bomb_grid)
    
    # 4. 중력
    bomb_grid = gravity(bomb_grid)

    # 5. 폭발
    bomb_grid = bomb(bomb_grid)


count = 0
for row in range(n):
    for col in range(n):
        if bomb_grid[row][col] != 0:
            count += 1

print(count)
