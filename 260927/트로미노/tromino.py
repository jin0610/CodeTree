N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def in_range(n, m):
    return n >= 0 and n < N and m >= 0 and m < M

for n in range(N):
    for m in range(M):
    
        # 3 x 1
        if in_range(n - 1, m) and in_range(n + 1, m):
            answer = max(answer, grid[n - 1][m] + grid[n][m] + grid[n + 1][m])
        
        # 1 x 3
        if in_range(n, m - 1) and in_range(n, m + 1):
            answer = max(answer, grid[n][m - 1] + grid[n][m] + grid[n][m + 1])

        # ㄱ
        if in_range(n, m - 1) and in_range(n + 1, m):
            answer = max(answer, grid[n][m - 1] + grid[n][m] + grid[n + 1][m])

        # ㄴ
        if in_range(n - 1, m) and in_range(n, m + 1):
            answer = max(answer, grid[n - 1][m] + grid[n][m] + grid[n][m + 1])
        
        # r
        if in_range(n - 1, m + 1) and in_range(n - 1, m):
            answer = max(answer, grid[n - 1][m] + grid[n][m] + grid[n - 1][m + 1])

        # ㄴ 반대
        if in_range(n, m - 1) and in_range(n - 1, m):
            answer = max(answer, grid[n][m - 1] + grid[n][m] + grid[n - 1][m])

print(answer)
        
        