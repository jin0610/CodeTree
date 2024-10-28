import sys

arr = [[0] * 2000 for _ in range(2000)]

x1, y1, x2, y2 = map(lambda x : int(x) + 1000, input().split())
a1, b1, a2, b2 = map(lambda x : int(x) + 1000, input().split())

# 두 사각형이 겹친 경우
if x1 >= a1 and x2 <= a2 and y1 >= b1 and y2 <= b2:
    print(0)
    sys.exit(0)

# 첫번째 사각형 
for x in range(x1, x2):
    for y in range(y1, y2):
        arr[x][y] += 1

# 두번째 사각형
for x in range(a1, a2):
    for y in range(b1, b2):
        arr[x][y] += 2

min_x, min_y, max_x, max_y = 2000, 2000, -1000, -1000
for x in range(2000):
    for y in range(2000):
        if arr[x][y] == 1:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(min_x, min_y, max_x, max_y)
print((max_x - min_x + 1) * (max_y-min_y + 1))