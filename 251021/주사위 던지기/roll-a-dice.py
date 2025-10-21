N, M, r, c = map(int, input().split())
grid = [
    [0 for _ in range(N)]
    for _ in range(N)
]
directions = list(input().split())

r, c = r - 1, c - 1
dirs = { # r, c
    'L' : (0, -1),
    "R" : (0, 1),
    "U" : (-1, 0),
    "D" : (1, 0)
}

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

# 윗면, 정면, 앞면
dice = [1, 2, 3]
# L 3 2 6 -> L 6 2 4, idx 0과 idx 2을 바꾸고 7 - dice[2]
# R 4 2 1 -> R, idx 0과 idx 2을 바꾸고 7 - dice[0]
# U 2 6 3 -> U, idx 0과 idx 1을 바꾸고 7- dice[1]
# D 5 1 3 -> D, idx 0과 idx 1을 바꾸고 7- dice[0]
# 아래 찍히는 숫자는 7-dice[0]
grid[r][c] = 6
for d in directions:
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    if in_range(nr, nc):    # 범위내라면 주사위를 굴리고 찍기
        if d == "L":
            dice[0], dice[2] = dice[2], dice[0]
            dice[2] = 7 - dice[2]
        elif d == "R":
            dice[0], dice[2] = dice[2], dice[0]
            dice[0] = 7 - dice[0]
        elif d == "U":
            dice[0], dice[1] = dice[1], dice[0]
            dice[1] = 7 - dice[1]
        else:
            dice[0], dice[1] = dice[1], dice[0]
            dice[0] = 7 - dice[0]
            
        grid[nr][nc] = 7 - dice[0]
        r, c = nr, nc

result = 0
for n in range(N):
    result += sum(grid[n])

print(result)