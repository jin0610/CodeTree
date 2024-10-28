arr = [[0] * 2000 for _ in range(2000)]

x1, y1, x2, y2 = map(lambda x : int(x) + 1000, input().split())
a1, b1, a2, b2 = map(lambda x : int(x) + 1000, input().split())

for x in range(x1, x2):
    for y in range(y1, y2):
        arr[x][y] = 1

for x in range(a1, a2):
    for y in range(b1, b2):
        arr[x][y] = 2

min_x, min_y, max_x, max_y = x1, y1, x2, y2
for x in range(x1, x2):
    for y in range(y1, y2):
        if arr[x][y] == 1:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
  

print((max_x - min_x) * (max_y-min_y))