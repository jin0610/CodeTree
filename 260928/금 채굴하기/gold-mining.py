N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def get_cost(k):
    return k ** 2 + (k + 1) ** 2

def get_count_of_golds(x, y, k):
    golds = 0
    for i in range(N):
        for j in range(N):
            if abs(x-i) + abs(y-j) <= k:
                golds += grid[i][j]   
    return golds

answer = 0
for i in range(N):
    for j in range(N):
        for k in range(2 * (N-1)+1):

            count_of_golds = get_count_of_golds(i, j, k)
            if get_cost(k) <= count_of_golds * M:
                answer = max(answer, count_of_golds)

print(answer)

