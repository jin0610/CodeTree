N, M, K = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(N)]

# 연속한 부분의 끝 점 찾기
def find_bomb_end_row(r, c, num):
    for end_row in range(r + 1, N):
        if numbers_2d[end_row][c] != num:
            return end_row - 1
    return len(numbers_2d[r]) - 1

# 폭탄 터지기
def bomb():
    for c in range(N):
        for r in range(N):
            if numbers_2d[r][c] == 0:
                continue
            end_row = find_bomb_end_row(r, c, numbers_2d[r][c])
            if end_row - r + 1 >= M:
                for row in range(r, end_row + 1):
                    numbers_2d[row][c] = 0
    gravity()

# 회전하기
def rotation():
    global numbers_2d
    temp = [
        [ 0 for _ in range(N)]
        for _ in range(N)
    ]
    for r in range(N):
        for c in range(N):
            temp[c][N - r - 1] = numbers_2d[r][c]

    numbers_2d = [
        temp[i][:] for i in range(N)
    ]
    gravity()

# 중력
def gravity():
    global numbers_2d
    for c in range(N):
        for r in range(N - 1, 0, -1):
            if numbers_2d[r][c] == 0:
                nr = r - 1
                while nr >= 0:
                    if numbers_2d[nr][c] != 0:
                        numbers_2d[r][c] = numbers_2d[nr][c]
                        numbers_2d[nr][c] = 0
                        break
                    else:
                        nr -= 1
                    
for _ in range(K):
    bomb()
    rotation()
bomb()

cnt = 0
for i in range(N):
    for j in range(N):
        if numbers_2d[i][j] != 0:
            cnt += 1
print(cnt)