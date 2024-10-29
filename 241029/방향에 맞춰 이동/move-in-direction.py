N = int(input())

# W S N E
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
direct = ['W', 'S', 'N', 'E']
x, y = 0, 0
for _ in range(N):
    d, l = input().split()
    l = int(l)
    idx = direct.index(d)
    x, y = x + dx[idx] * l, y + dy[idx] * l

print(x, y)