D = input()

# L : 반시계방향 R : 시계방향
# 시계방향 (N E S W)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

i = 0
x, y = 0, 0
for d in D:
    if d == 'L':
        i = i - 1
    elif d == 'R':
        i = i + 1
    else:
        x, y = x + dx[i], y + dy[i]
print(x, y)