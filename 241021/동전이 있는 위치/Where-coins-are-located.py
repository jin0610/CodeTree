n, m = list(map(int, input().split()))

arr = [[0] * n for i in range(n)]

for i in range(m):
    r, c = list(map(int, input().split()))
    arr[r-1][c-1] = 1

for i in range(n):
    print(*arr[i])