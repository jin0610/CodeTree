N = int(input())

# W S N E
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
x, y = 0, 0

for n in range(N):
    d, i = input().split()
    i = int(i)

    if d == "W":
        x, y = x + dx[0] * i, y + dy[0] * i
    elif d == "S":
        x, y = x + dx[1] * i, y + dy[1] * i
    elif d == "N":
        x, y = x + dx[2] * i, y + dy[2] * i
    else:
        x, y = x + dx[3] * i, y + dy[3] * i

print(x, y)