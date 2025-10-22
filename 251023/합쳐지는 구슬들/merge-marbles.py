N, M, T = map(int,input().split())

#구슬 정보
marbles = []

# 방향 설정
dirs = {"U":0, 'R':1, "D": 2, "L":3}
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

# 구슬 정보 저장
for m in range(M):
    r, c, d, w = input().split()
    r, c, d, w = int(r) - 1, int(c) - 1, dirs[d], int(w)
    marbles.append((m + 1, r, c, d, w))

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

# 각 구슬의 움직임
def move_marbles(r, c, d):
    nr, nc = r + drs[d], c + dcs[d]
    if not in_range(nr, nc):
        nr, nc = r, c
        d = (d + 2) % 4
    return (nr, nc, d)

# 구슬의 충돌이 발생한 경우
def collide_marble(collide_marbles):
    new_num, new_dir, new_weight = 0, 0, 0
    for marble in collide_marbles:
        num, d, w = marble
        new_weight += w     # 무게는 겹쳐진 모든 구슬의 무게의 합
        if num > new_num:   
            new_num = num   # 번호는 가장 큰 번호
            new_dir = d     # 방향은 가장 큰 번호의 방향

    return new_num, new_dir, new_weight

# 1초마다의 움직임
def move():
    global marbles

    marbles_cnt = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]

    # 구슬의 새로운 위치를 저장
    new_position = {}
    for marble in marbles:
        idx, r, c, d, w = marble
        r, c, d = move_marbles(r, c, d)
        if marbles_cnt[r][c] == 0:
            new_position[(r, c)] = [(idx, d, w)]
        else:
            new_position[(r, c)].append((idx, d, w))
        marbles_cnt[r][c] += 1

    marbles = []
    for key, values in new_position.items():
        r, c = key
        # 구슬의 충돌이 발생한 경우
        if marbles_cnt[r][c] >= 2:
            i, d, w = collide_marble(values)
        else:
            i, d, w = values[0]

        marbles.append((i, r, c, d, w))

for _ in range(T):
    move()

max_weight = 0
for i, r, c, d, w in marbles:
    if w > max_weight:
        max_weight = w
print(len(marbles), max_weight)