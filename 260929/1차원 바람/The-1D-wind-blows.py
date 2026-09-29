n, m, q = map(int, input().split()) # N x M, Q: 바람이 불어온 횟수
grid = [list(map(int, input().split())) for _ in range(n)]

def check(r, nr):
    for i in range(m):
        if grid[r][i] == grid[nr][i]:
            return True
    return False

def shift(r, d, check_d):
    if d == "L":
        temp = grid[r][-1]
        for i in range(m - 1, 0, -1):
            grid[r][i] = grid[r][i - 1]
        grid[r][0] = temp
        nd = "R"

    else:
        temp = grid[r][0]
        for i in range(m - 1):
            grid[r][i] = grid[r][i + 1]
        grid[r][-1] = temp
        nd = "L"
    
    if check_d == "U":
        if r - 1 >= 0 and check(r, r - 1):
            shift(r - 1, nd, check_d)
        else:
            return
    else:
        if r + 1 < n and check(r, r + 1):
            shift(r + 1, nd, "D")
        else:
            return

for _ in range(q):
    r, d = input().split() # (바람에 영향을 받는 행 번호, 바람이 불어오는 방향)
    r = int(r) - 1
    if d == "L":
        temp = grid[r][-1]
        for i in range(m - 1, 0, -1):
            grid[r][i] = grid[r][i - 1]
        grid[r][0] = temp
        nd = "R"
    else:
        temp = grid[r][0]
        for i in range(m - 1):
            grid[r][i] = grid[r][i + 1]
        grid[r][-1] = temp
        nd = "L"

    if r - 1 >= 0 and check(r, r - 1):
        shift(r - 1, nd, "U")
    
    if r + 1 < n and check(r, r + 1):
        shift(r + 1, nd, "D")

for i in range(n):
    print(*grid[i])