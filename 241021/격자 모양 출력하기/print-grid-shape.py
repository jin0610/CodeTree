N, M = list(map(int, input().split()))

result = [[0] * N for _ in range(N)]

for m in range(M):
    r, c = list(map(int, input().split()))
    result[r-1][c-1] = r*c

for n in range(N):
    print(*result[n])