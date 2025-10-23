n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
area_grid = [   # 초토화된 영역을 표시하기 위한 grid
    [0 for _ in range(n)]
    for _ in range(n)
]

# 폭탄의 3가지 유형
bomb_types = {
    1 : [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    2 : [(-1, 0), (1, 0), (0, 1), (0, -1)],
    3 : [(-1, -1), (-1, 1), (1, 1), (1, -1)]
}

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

bomb_count = 0  # 폭탄의 수
bomb_pos = []   # 폭탄 위치
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            area_grid[i][j] = 1
            bomb_pos.append((i, j))
            bomb_count += 1
 


def count_areas(bomb_combination):
    global bomb_types, bomb_pos, bomb_count, area_grid

    for i in range(bomb_count):
        r, c = bomb_pos[i]  # bomb 위치
        bomb_type = bomb_combination[i] # 폭탄 유형
        for area_r, area_c in bomb_types[bomb_type]:    
            nr, nc = r + area_r, c + area_c
            if in_range(nr, nc):
                area_grid[nr][nc] = 1

    count = 0 # 초토와되는 영역의 수
    for i in range(n):
        for j in range(n):
            if area_grid[i][j] == 1:
                count += 1

                # area_gird 초기화
                if (i, j) not in bomb_pos:
                    area_grid[i][j] = 0
    return count

bombs = []  # 폭탄 조합
answer = 0  # 초토화되는 영역의 수
def choice_bomb(num):
    global bombs, answer

    if len(bombs) == bomb_count:
        answer = max(answer, count_areas(bombs))
        return

    for i in range(1, 4):   # 3가지의 폭탄이므로 범위는 (1, 4)
        bombs.append(i)
        choice_bomb(num + 1)
        bombs.pop()

    return

choice_bomb(1)
print(answer)
