R, C = map(int, input().split())

grid = [ list(input().split()) for _ in range(R)]

result = 0
for i in range(R):
    for j in range(C):
        for r in range(i + 1, R-1):
            for c in range(j + 1, C-1):
                if grid[0][0] != grid[i][j] and grid[i][j] != grid[r][c] and grid[r][c] != grid[R-1][C-1]:
                    result += 1

print(result)