N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

count = 0

for n in range(N):
    cnt = 0
    curr = grid[n][0]
    for i in range(N):
        next = grid[n][i]
        if curr == next:
            cnt += 1
            if cnt >= M:
                count += 1
                break
        else:
            cnt = 1
            curr = next

    cnt = 0
    curr = grid[0][n]
    for i in range(N):
        next = grid[i][n]
        if curr == next:
            cnt += 1
            if cnt >= M:
                count += 1
                break
        else:
            cnt = 1
            curr = next

print(count)