N = int(input())
grid = [    # 숫자가 적힌 grid
    list(map(int, input().split()))
    for _ in range(N)
]
grid_dir = [    # 방향이 적힌 grid
    list(map(int, input().split()))
    for _ in range(N)
]

r, c = map(int, input().split())
dirs = {
    1 : (-1, 0),
    2 : (-1, 1),
    3 : (0, 1),
    4 : (1, 1),
    5 : (1, 0),
    6 : (1, -1),
    7 : (0, -1),
    8 : (-1, -1),
}

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N
    
def get_pos(r, c):
    num = grid[r][c]
    d = grid_dir[r][c]

    pos = [] # 이동 가능한 pos
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    while True:
        if not in_range(nr, nc):
            break
        
        if grid[nr][nc] > num:
            pos.append((nr, nc))

        nr, nc = nr + dirs[d][0], nc + dirs[d][1]
    return pos
    
nums = []           # 간 곳
possible_pos = []   # 갈 수 있는 곳
answer = 0
def move(r, c):
    global nums, answer
    possible_pos = get_pos(r, c)

    # 주위에 더이상 갈 곳이 없으면 종료
    if len(possible_pos) == 0:
        answer = max(answer, len(nums))
        return

    for pos in possible_pos:
        nums.append(pos)
        move(pos[0], pos[1])
        nums.pop()
    
    return

move(r - 1, c - 1)
print(answer)