import sys
strs = input()

# N, E S W
dx, dy = [0, 1, 0, -1], [1,0,-1,0]
x, y = 0, 0
idx= 0
sec = 0
for s in strs:
    if(s == "L"):
        idx = (idx + 1) % 4
    elif(s == "R"):
        idx = (idx - 1) % 4
    else:
        x, y = x + dx[idx], y + dy[idx]
    sec = sec + 1
    if(x == 0 and y == 0):
        print(sec)
        sys.exit(0)
print(-1)