ss = list(input())

# N, E, S, W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
idx = 0
for s in ss:
    if s == 'L':
        idx = (idx - 1) % 4
    elif s == 'R':
        idx = (idx + 1) % 4
    else:
        x = x + dx[idx]
        y = y + dy[idx]
    
print(x, y)