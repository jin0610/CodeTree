N = int(input()) # 격자
mirror = [list(input()) for _ in range(N)]

K = int(input()) # 레이저 쏘는 위치

# / : 90도, \ : -90 
# 위 오른 아래 왼
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 격자 범위
def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

# 시작점 위치
if (K-1) // N == 0:
    x, y = 0, (K - 1) % N
    idx = 0
elif (K-1) // N == 1:
    x, y = (K - 1) % N, (N - 1)
    idx = 1
elif (K-1) // N == 2:
    x, y = (N - 1), (K - 1) % N
    idx = 2
else:
    x, y = (K - 1) % N, 0
    idx = 3

# 거울에 튕기는 횟수 세기
# 위 오른 아래 왼
mirror_dict1 = {0:2, 1:3, 2:0, 3:1} 

cnt = 0
while in_range(x, y):

    if mirror[x][y] == '\\': # 위(0) -> 오른(1) / 오른(1) -> 위(1) / 왼쪽(3)-> 아래(2) / 아래(2) -> 왼쪽(3)
        if idx == 0 or idx ==1:
            idx = 1 - idx
        else:
            idx = 5 - idx
    else: # 위(0) - 오른(1) / 왼(3) -> 아래(2) / 아래(2) -> 왼(3) / 오른(1) -> 위(0)
        if idx == 0 or idx ==1:
            idx = 3 - idx
       
    cnt += 1
    x, y = x + dx[idx], y + dy[idx]
    idx = mirror_dict1[idx]



print(cnt)