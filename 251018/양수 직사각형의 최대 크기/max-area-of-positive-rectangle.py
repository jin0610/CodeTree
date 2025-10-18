import sys

N, M = map(int, input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

def isPositiveSum(rect):
    x1, y1, x2, y2 = rect

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if grid[y][x] < 0:
                return False

    return True

answer = -1
for y1 in range(N):
    for x1 in range(M):
        for y2 in range(y1, N):
            for x2 in range(x1, M):
                if isPositiveSum((x1, y1, x2, y2)):
                    size = (x2 - x1 + 1) * (y2 - y1 + 1)
                    answer = max(answer, size)

print(answer)