arr = [[0] * 2000 for _ in range(2000)]

for i in range(1, 4):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = i

result = 0
for i in range(2000):
    result = result + arr[i].count(1) + arr[i].count(2)

print(result)