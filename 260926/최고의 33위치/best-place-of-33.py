n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def find_coin(i, j):
    count = 0
    for y in range(i, i + 3):
        count += sum(grid[y][j : j + 3])
    return count

answer = 0
for i in range(n-2):
    for j in range(n-2):
        answer = max(answer, find_coin(i, j))

print(answer)
