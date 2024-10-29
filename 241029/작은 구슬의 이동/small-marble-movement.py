n, t= list(map(int, input().split()))
r, c, d = input().split()

# U R L D
dc, dr = [0, 1, -1, 0], [-1, 0, 0, 1]
idx = ["U", "R", "L", "D"]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

sec = 0
direct = idx.index(d)
r, c = int(r)-1, int(c)-1

while sec <t:
    nr, nc = r + dr[direct], c+ dc[direct]
    if in_range(nr,nc):
        r, c = nr, nc
    else:
        direct = 3 - direct
    sec += 1
    

print(r + 1, c + 1)