import sys
N = int(input())

info = [input().split() for _ in range(N)]

# W S N E
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
dic = {'W' : 0, 'S' : 1, 'N' : 2, 'E' : 3}

x, y = 0, 0
s = 0
for direc, dis in info:
    

    dis = int(dis)
    idx = dic[direc]

    for i in range(dis):
        x , y = x + dx[idx], y + dy[idx]
        s = s + 1
    
        if(x == 0 and y == 0):
            print(s)
            sys.exit(0)
    

print(-1)