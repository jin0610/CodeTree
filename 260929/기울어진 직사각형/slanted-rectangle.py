N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

def get_number_sum(x, y, w, h):
    _sum = 0
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [w, h, w, h]

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
            if in_range(x, y):
                _sum += grid[x][y]
            else:
                return 0

    return _sum

max_sum = 0
for x in range(N):
    for y in range(N):
        for w in range(1, N):
            for h in range(1, N):
                max_sum = max(max_sum, get_number_sum(x, y, w, h))

print(max_sum)