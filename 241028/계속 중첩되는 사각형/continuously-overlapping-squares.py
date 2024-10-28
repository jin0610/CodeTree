N = int(input())

arr = [[0] * 200 for _ in range(200)]
for n in range(N):
    x1, y1, x2, y2 = map(lambda x : int(x) + 100, input().split())

    if n % 2 == 0: # 처음은 빨간색(1)
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 1
    else:           # 처음은 파란색(2)
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 2

blue = 0    
for i in range(200):
    for j in range(200):
        if arr[i][j] == 2:
            blue += 1

print(blue)