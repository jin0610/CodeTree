import sys
input = sys.stdin.readline

# 위 오른 아래 왼
directions = ["U", "R", "D", "L"]
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y, N):
    return x >= 0 and x < N and y >= 0 and y < N

def move_beads(beads, n):
    pos_dict = {}
    dir_dict = {}
    
    for x, y, d in beads:
        d_idx = directions.index(d)
        nx, ny = x + dxs[d_idx], y + dys[d_idx]
        if not in_range(nx, ny, n):
            nx, ny = x, y
            d = directions[(d_idx + 2) % 4]
            
        # 새로운 위치 저장
        pos = (nx, ny)
        if pos not in pos_dict.keys():
            pos_dict[pos] = 1
            dir_dict[pos] = d
        else:
            pos_dict[pos] += 1

    new_beads = []
    for key, value in pos_dict.items():
        if value == 1:
            new_beads.append([key[0], key[1], dir_dict[key]])
    return new_beads


def move(n, m):
    beads = []

    for _ in range(m):
        x, y, d = list(input().split())
        x, y = int(x) - 1, int(y) - 1
        beads.append([x, y, d])

    for _ in range(2 * n):
        if len(beads) == 0:
            break
        beads = move_beads(beads, n)
    
    print(len(beads))

T = int(input())  
for _ in range(T):
    N, M = map(int, input().split())
    move(N, M)