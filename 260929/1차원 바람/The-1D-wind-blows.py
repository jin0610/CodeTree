n, m, q = map(int, input().split()) # N x M, Q: 바람이 불어온 횟수
grid = [list(map(int, input().split())) for _ in range(n)]

# 두 행의 같은 열에 같은 숫자가 있는지 확인
def check(r, nr):
    for i in range(m):
        if grid[r][i] == grid[nr][i]:
            return True
    return False

# 방향 전환
def flip(curr_d):
    return "R" if curr_d == "L" else "L"

# 이동 함수
def shift(r, d):
    if d == "L":
        temp = grid[r][-1]
        for i in range(m - 1, 0, -1):
            grid[r][i] = grid[r][i - 1]
        grid[r][0] = temp

    else:
        temp = grid[r][0]
        for i in range(m - 1):
            grid[r][i] = grid[r][i + 1]
        grid[r][-1] = temp

def simulate(r, d):
    # 최초 행 이동
    shift(r, d)

    # 방향 전환
    next_d = flip(d)

    # 위쪽 전파
    curr_d = next_d
    for nr in range(r - 1, -1, -1):
        if not check(nr + 1, nr):
            break

        shift(nr, curr_d)
        curr_d = flip(curr_d)

    # 아래쪽 전파
    curr_d = next_d
    for nr in range(r + 1, n):
        if not check(nr - 1, nr):
            break

        shift(nr, curr_d)
        curr_d = flip(curr_d)

for _ in range(q):
    r, d = input().split() # (바람에 영향을 받는 행 번호, 바람이 불어오는 방향)
    r = int(r) - 1
    
    simulate(r, d)

for i in range(n):
    print(*grid[i])