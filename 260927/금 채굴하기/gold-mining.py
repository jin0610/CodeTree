N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (0, 1), (0, 0), (1, 0), (0, -1)]

def in_range(i, j):
    return i >= 0 and i < N and j >= 0 and j < N

def cal_cost(k):
    return k ** 2 + (k + 1) ** 2

def count_gold(row, col, k):
    count = 0
    for i in range(N):
        for j in range(N):
            if abs(row - i) + abs(col - j) <= k:
                count += grid[i][j]
    return count


answer = 0

for  i in range(N):
    for j in range(N):
        for k in range(2 * (N - 1) + 1):
            golds = count_gold(i, j,k)

            if golds * M >= cal_cost(k):
                answer = max(answer, golds)

print(answer)