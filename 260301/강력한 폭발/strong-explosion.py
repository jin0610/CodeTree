n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
bombs_dict = {
    1 : [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    2 : [(-1, 0), (0, 1), (1, 0), (0, -1)],
    3 : [(-1, -1), (-1, 1), (1, 1), (1, -1)]
}

bomb_cnt = 0
bomb_location = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_cnt += 1
            bomb_location.append((i, j))

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb():
    global selected_bomb, bombs_dict, bomb_location

    temp = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(bomb_cnt):
        bomb_type = selected_bomb[i]    # 폭탄 유형
        by, bx = bomb_location[i]       # 폭탄 위치

        if temp[by][bx] == 0:
            temp[by][bx] = 1
            count += 1
        
        for j in range(4):
            nx, ny = bx + bombs_dict[bomb_type][j][1], by + bombs_dict[bomb_type][j][0]
            if in_range(nx, ny):
                if temp[ny][nx] == 0:
                    count += 1
                
                temp[ny][nx] = 1

    return count

answer = 0
selected_bomb = []
def backtracking(curr_n):
    global selected_bomb, bomb_cnt, answer

    if curr_n == bomb_cnt:
        answer = max(answer, bomb())
        return

    for i in range(1, 4):
        selected_bomb.append(i)
        backtracking(curr_n + 1)
        selected_bomb.pop()

backtracking(0)
print(answer)