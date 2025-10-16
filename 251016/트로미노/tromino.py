N, M = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

# 위, 오른, 아래, 왼 (시계방향)
dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0]
result = 0

# 1x3 블럭
for n in range(N):
    for m in range(1, M-1):
        nums = sum(grid[n][m-1:m+2])
        result = max(result, nums)

# 3x1 블럭
for m in range(M):
    for n in range(1, N-1):
        nums = grid[n-1][m] + grid[n][m] + grid[n+1][m]
        result = max(result, nums)

# ㄴ 블럭
for n in range(N):
    for m in range(M):
        nums = [0, 0, 0, 0] # ㄴ을 시계방향으로 돌린 것
        for i in range(4):
            if n + dc[i] < 0 or n + dc[i] >= N or m + dr[i] < 0 or m + dr[i] >= M or \
            n + dc[(i + 1) % 4] < 0 or n + dc[(i + 1) % 4] >= N or m + dr[(i + 1) % 4] < 0 or m + dr[(i + 1) % 4] >= M:
                continue

            nums[i] = grid[n][m] + grid[n + dc[i]][m + dr[i]] + grid[n + dc[(i + 1) % 4]][m + dr[(i + 1) % 4]]

        result = max(result, max(nums))

print(result)