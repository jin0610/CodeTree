R, C = map(int, input().split())
grid = [input().split() for _ in range(R)]

count = 0

for i in range(1, R):
    for j in range(1, C):
        for r in range(i + 1, R - 1):
            for c in range(j + 1, C - 1):
                if grid[i][j] != grid[0][0] and grid[r][c] != grid[R-1][C-1]:
                    if grid[r][c] != grid[i][j]:
                        count += 1

print(count)