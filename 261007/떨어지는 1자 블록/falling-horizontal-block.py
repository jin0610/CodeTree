n, m , k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

row = 0
did_touch = False
while True:

    for col in range(k - 1, k - 1 + m):
        if row + 1 < n and grid[row + 1][col] == 1:
            did_touch = True
            break
        
    if did_touch or row >= n - 1:
        grid[row][k - 1 : k - 1 + m] = [1] * m
        break

    row += 1

for i in range(n):
    print(*grid[i])