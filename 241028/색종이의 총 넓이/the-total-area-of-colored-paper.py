N =int(input())

arr = [[0] * 200 for _ in range(200)]

for n in range(N):
    x, y = map(int, input().split())
    x, y = x + 100, y + 100

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            arr[i][j] = 1

result = 0
for i in range(200):
    result = result + arr[i].count(1)
print(result)