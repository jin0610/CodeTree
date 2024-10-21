n, m = list(map(int, input().split()))

maps = [[0]*m]*n

num = 1
for i in range(n):
    for j in range(m):
        maps[i][j] = num
        num = num + 1
    print(*maps[i])