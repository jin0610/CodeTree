### 자리수 단위로 완전 탐색 / 숨은 단어 찾기 2
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < M

# [nw, n, ne, e, es, s, sw, w]
dxs, dys = [-1, 0, 1, 1, 1, 0, -1, -1], [-1, -1, -1, 0, 1, 1, 1, 0]

cnt = 0
for n in range(N):
    for m in range(M):
        if arr[n][m] != "L":
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = n + dx, m + dy
            if in_range(nx, ny) and arr[nx][ny] == "E":
                nx, ny = n + 2*dx, m + 2*dy
                if in_range(nx, ny) and arr[nx][ny] == "E":
                    cnt += 1

print(cnt)


