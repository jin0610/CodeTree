n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_bomb_range(r, c):
    return 0 <= r < n and 0 <= c < n

def cross_bomb_shape(center_r, center_c, grid):
    bomb_range = grid[center_r][center_c]

    # 폭탄 터트리기
    for dr, dc in zip(drs, dcs):
        for l in range(bomb_range):
            nr, nc = center_r + dr * l, center_c + dc * l
            if in_bomb_range(nr, nc):
                grid[nr][nc] = 0
    # print("bomb!")
    # for i in range(n):
    #     print(*grid[i])
    # 중력 작용
    for c in range(n):
        for r in range(n - 1, 0, -1):
            if grid[r][c] == 0:
                nr = r - 1
                while nr >= 0:
                    if grid[nr][c] == 0:
                        nr -= 1
                    grid[r][c] = grid[nr][c]
                    grid[nr][c] = 0
                    break
    # print("gravity!")
    # for i in range(n):
    #     print(*grid[i])
    # 인접한 두 블럭의 숫자가 동일한 경우 
    cnt = 0
    for r in range(n):
        for c in range(n - 1):
            if grid[r][c] == 0:
                continue
            if grid[r][c] == grid[r][c + 1]:
                cnt += 1
    
    for c in range(n):
        for r in range(n - 1):
            if grid[r][c] == 0:
                continue
            if grid[r][c] == grid[r + 1][c]:
                cnt += 1

    return cnt

result = 0
# result = cross_bomb_shape(1, 1, grid)
for r in range(n):
    for c in range(n):
        tmp = [row[:] for row in grid]
        cnt = cross_bomb_shape(r, c, tmp)
        # print(r,c,cnt)
        result = max(result, cnt)
print(result)