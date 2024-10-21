n, m = list(map(int, input().split()))

result = [[0] * n for _ in range(n)]

cnt = 1
for i in range(m):
    r, c =  list(map(int, input().split()))
    result[r-1][c-1] = cnt
    cnt += 1

for i in range(n):
    print(*result[i])