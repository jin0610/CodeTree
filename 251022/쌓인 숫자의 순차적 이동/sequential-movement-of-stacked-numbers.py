n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

grid_dict = {}
for r in range(n):
    for c in range(n):
        grid_dict[(r, c)] = [grid[r][c]]

# 8방향
drs = [-1, -1, -1, 0, 1, 1, 1, 0]
dcs = [-1, 0, 1, 1, 1, 0, -1, -1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def move_num(pos, num):
    global grid_dict
    
    max_num, max_pos = -1, pos
    for dr, dc in zip(drs, dcs):
        nr, nc = pos[0] + dr, pos[1] + dc
        if in_range(nr, nc):
            if grid_dict[(nr, nc)] and max(grid_dict[(nr, nc)]) > max_num:
                max_num = max(grid_dict[(nr, nc)])
                max_pos = (nr, nc)
    
    temp = []
    while True:
        number = grid_dict[pos].pop()
        temp.append(number)
        if number == num:
            break
    
    while temp:
        grid_dict[max_pos].append(temp.pop())
    
    

def move():
    global grid_dict, move_nums
    for num in move_nums:
        for key, value in grid_dict.items():
            if num in value:
                move_num(key, num)
                break
                


move()

for r in range(n):
    for c in range(n):
        if len(grid_dict[(r, c)]) == 0:
            print("None")
        else:
            print(*grid_dict[(r, c)][::-1])