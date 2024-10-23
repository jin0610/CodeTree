N,M = list(map(int, input().split()))

arr = [[0] * N for _ in range(N)]
 
# 상하좌우
dx, dy = [0,0,-1,1],[-1,1,0,0]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

# 색칠
for m in range(M):
    r, c = list(map(int, input().split()))
    r, c = r-1, c-1
    arr[r][c] = 1

    cnt = 0
    for x, y in zip(dx, dy):
        nx, ny = r + x, c + y

        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt = cnt + 1

    if(cnt == 3):
        print(1)
    else:
        print(0)