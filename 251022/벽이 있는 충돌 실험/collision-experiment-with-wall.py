import sys
input = sys.stdin.readline

# 위 오른 아래 왼
directions = {'U':0, 'R':1, 'D':2, 'L':3}
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def move_beads(pos_x, pos_y, dirs, n):
    pos_dict = {}
    dir_dict = {}
    
    for x, y, d in zip(pos_x, pos_y, dirs):
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

    beads_pos_x = []
    beads_pos_y = []
    beads_dir = []

    for (x, y), cnt in pos_dict.items():
        if cnt == 1:
            beads_pos_x.append(x)
            beads_pos_y.append(y)
            beads_dir.append(dir_dict[(x, y)])
    return beads_pos_x, beads_pos_y, beads_dir


def move(n, m):
    beads_pos_x = []
    beads_pos_y = []
    beads_dir = []

    for _ in range(m):
        x, y, direction = input().split()
        x, y, d = int(x) - 1, int(y) - 1, directions[direction]
        beads_pos_x.append(x)
        beads_pos_y.append(y)
        beads_dir.append(d)

    for _ in range(2 * n):
        # 구슬이 없으면 종료
        if not beads_pos_x:
            break

        # 방향이 R이나 L이고 모든 행(x)이 다를 경우 break
        if len(set(beads_pos_x)) == n and 0 not in beads_dir and 2 not in beads_dir:
            break

        # 뱡향이 U이나 D이고 모든 열(y)이 다 다를 경우 break
        if len(set(beads_pos_y)) == n and 1 not in beads_dir and 3 not in beads_dir:
            break

        beads_pos_x, beads_pos_y, beads_dir = move_beads(beads_pos_x, beads_pos_y, beads_dir, n)
    
    print(len(beads_pos_x))

T = int(input())  
for _ in range(T):
    N, M = map(int, input().split())
    move(N, M)