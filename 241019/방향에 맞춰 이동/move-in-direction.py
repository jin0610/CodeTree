N = int(input())

info =[]
for i in range(N):
    info.append(input().split())

dx, dy = 0,0
for d, n in info:
    n = int(n)
    if(d=="N"):
        dy = dy +n
    elif d == "S":
        dy = dy - n
    elif d == "W":
        dx = dx - n
    else:
        dx = dx + n

print(dx, dy)