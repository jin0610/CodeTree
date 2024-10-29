N, T = map(int, input().split())
ss = list(input())
nums = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < N

r = c = N // 2
idx = 0
result = nums[r][c]

for s in ss:
    if s == 'L':
        idx = (idx - 1) % 4
    elif s == 'R':
        idx = (idx + 1) % 4
    else:
        nr, nc = r + dr[idx], c + dc[idx]
        if in_range(nr, nc):
            r, c = nr, nc
            result += nums[r][c]
        else:
            pass

print(result)