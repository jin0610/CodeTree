import sys
input = sys.stdin.readline

# 위 오른 아래 왼
directions = {'U':0, 'R':1, 'D':2, 'L':3}
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def move_beads(beads, n):
    pos_dict = {}
    dir_dict = {}
    
    for x, y, d in beads:
        nx, ny = x + dxs[d], y + dys[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            nx, ny = x, y
            d = (d + 2) % 4
            
        # 새로운 위치 저장
        pos = (nx, ny)
        cnt = pos_dict.get(pos, 0) + 1
        pos_dict[pos] = cnt
        if cnt == 1:
            dir_dict[pos] = d

    new_beads = []
    for (x, y), cnt in pos_dict.items():
        if cnt == 1:
            bead = [x, y, dir_dict[(x, y)]]
            new_beads.append(bead)
    return new_beads


def move(n, m):
    beads = []

    for _ in range(m):
        x, y, direction = input().split()
        x, y = int(x) - 1, int(y) - 1
        d = directions[direction]
        beads.append([x, y, d])

    for _ in range(2 * n):
        if not beads:
            break
        beads = move_beads(beads, n)
    
    print(len(beads))

T = int(input())  
for _ in range(T):
    N, M = map(int, input().split())
    move(N, M)