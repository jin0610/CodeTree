import sys

N = int(input())

#  W S N E
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
direct = ["W", "S", "N", "E"]

sec = 0
x, y = 0,0

for _ in range(N):
    d, l = input().split()
    l = int(l)    

    di = direct.index(d)
    for i in range(l):
        x, y = x + dx[di], y + dy[di]
        sec += 1
        if x == 0 and y == 0:
            print(sec)
            sys.exit(0)

    

print(-1)