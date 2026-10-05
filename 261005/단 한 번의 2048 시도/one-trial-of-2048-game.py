grid = [list(map(int, input().split())) for _ in range(4)]
dir = input()

SIZE = 4

def move_grid_left(grid):
    for row in range(SIZE):
        # 1. 값 합치기
        pre_idx, cnt = 0, 1
        for col in range(1, SIZE):
            if grid[row][col] == 0:
                continue

            if grid[row][col] ==  grid[row][pre_idx]:
                cnt += 1
                if cnt >= 2:
                    grid[row][pre_idx] += grid[row][col]
                    grid[row][col] = 0
                    cnt = 0
            else:
                cnt = 1

            pre_idx = col

        # 2. 이동
        temp = None
        for col in range(SIZE):
            if temp is None and grid[row][col] == 0:
                temp = col

            if temp is not None and grid[row][col] != 0:
                grid[row][temp] = grid[row][col]
                grid[row][col] = 0
                temp += 1

def move_grid_right(grid):
    for row in range(SIZE):
        # 1. 값 합치기
        pre_idx, cnt = SIZE - 1, 1
        for col in range(SIZE - 2, -1, -1):
            if grid[row][col] == 0:
                continue

            if grid[row][col] == grid[row][pre_idx]:
                cnt += 1
                if cnt >= 2:
                    grid[row][pre_idx] += grid[row][col]
                    grid[row][col] = 0
                    cnt = 0
            else:
                cnt = 1
            pre_idx = col

        # 2. 이동
        temp = None
        for col in range(SIZE -1, -1, -1):
            if temp is None and grid[row][col] == 0:
                temp = col
            
            if temp is not None and grid[row][col] != 0:
                grid[row][temp] = grid[row][col]
                grid[row][col] = 0
                temp -= 1

def move_grid_up(grid):
    for col in range(SIZE):
        # 1. 값 합치기
        pre_idx, cnt = 0, 1
        for row in range(1, SIZE):
            if grid[row][col] == 0:
                continue

            if grid[pre_idx][col] == grid[row][col]:
                cnt += 1
                if cnt >= 2:
                    grid[pre_idx][col] += grid[row][col]
                    grid[row][col] = 0
                    cnt = 0
            else:
                cnt = 1
            pre_idx = row

        # 2. 이동
        temp = None
        for row in range(SIZE):
            if temp is None and grid[row][col] == 0:
                temp = row
            
            if temp is not None and grid[row][col] != 0:
                grid[temp][col] = grid[row][col]
                grid[row][col] = 0
                temp += 1

def move_grid_down(grid):
    for col in range(SIZE):
        # 1. 값 합치기
        pre_idx, cnt = SIZE - 1, 1
        for row in range(SIZE - 2, -1, -1):
            if grid[row][col] == 0:
                continue

            if grid[pre_idx][col] == grid[row][col]:
                cnt += 1
                if cnt >= 2:
                    grid[pre_idx][col] += grid[row][col]
                    grid[row][col] = 0
                    cnt = 0
            else:
                cnt = 1
            pre_idx = row

        # 2. 이동
        temp = None
        for row in range(SIZE - 1, -1, -1):
            if temp is None and grid[row][col] == 0:
                temp = row
            
            if temp is not None and grid[row][col] != 0:
                grid[temp][col] = grid[row][col]
                grid[row][col] = 0
                temp -= 1

def print_grid(grid):
    for row in range(SIZE):
        print(*grid[row])

if dir == "L":
    move_grid_left(grid)
elif dir == "R":
    move_grid_right(grid)
elif dir == "U":
    move_grid_up(grid)
else:
    move_grid_down(grid)

print_grid(grid)