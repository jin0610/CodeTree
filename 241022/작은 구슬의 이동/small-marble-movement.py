n, t = list(map(int, input().split()))
r, c, d = input().split()


# U D R L
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
idx = {'U': 0, 'R' : 1, 'L' : 2, 'D' : 3}

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 1초에 한 칸씩 / 벽에 부딪히면 반대방향으로 뒤집힘(1초)
sec = 0
di = idx[d]
r, c = int(r)-1, int(c)-1

while sec != t:
    if in_range(r + dy[di], c + dx[di]):
        r, c = r + dy[di], c + dx[di]
    else:
        di = 3 - di
    sec = sec + 1
    

print(r+1, c+1)