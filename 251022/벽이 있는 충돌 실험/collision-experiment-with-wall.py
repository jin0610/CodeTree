T = int(input())

# 위 오른 아래 왼
# directions = {"U" : 0, "R":1, "D":2, "L": 3}
directions = ["U", "R", "D", "L"]
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

def move_beads(beads):
    new_positions = []
    new_directions = []
    pos_count = []
    
    for x, y, d in beads:
        d_idx = directions.index(d)
        nx, ny = x + dxs[d_idx], y + dys[d_idx]
        if not in_range(nx, ny):
            nx, ny = x, y
            d = directions[3 - d_idx]
        
        # 새로운 위치 저장
        pos = [nx, ny]
        if [nx, ny] not in new_positions:
            new_positions.append(pos)
            new_directions.append([d])
            pos_count.append(1)
        else:
            idx = new_positions.index(pos)
            pos_count[idx] += 1

    new_beads = []
    for i in range(len(pos_count)):
        if pos_count[i] == 1:
            new_bead = new_positions[i] + new_directions[i]
            new_beads.append(new_bead)
    return new_beads


def move(n, m):
    beads = []

    for _ in range(m):
        x, y, d = list(input().split())
        x, y = int(x) - 1, int(y) - 1
        beads.append([x, y, d])

    for _ in range(2*n):
        beads = move_beads(beads)
    
    print(len(beads))
    
for _ in range(T):
    N, M = map(int, input().split())
    move(N, M)