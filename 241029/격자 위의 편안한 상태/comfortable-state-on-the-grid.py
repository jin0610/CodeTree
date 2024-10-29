N,M = map(int, input().split())

maps = [[0] * N for _ in range(N)]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

# 상 하 좌 우
dx, dy = [0,0, -1, 1], [-1, 1, 0, 0]
result = 0

for m in range(M):
    r, c = map(lambda x : int(x) -1 , input().split())
    maps[r][c] = 1
    cnt = 0
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if in_range(nr, nc) and maps[nr][nc] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)