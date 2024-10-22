n = int(input())

maps = [list(map(int, input().split())) for i in range(n)]

# 상 하 좌 우
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# x, y범위
def in_range(x,y):
    return x >= 0 and x < n and y >=0 and y < n

# 주변 1의 개수 세기
def count1(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        try:
            if in_range(x, y) and maps[nx][ny] == 1:
                cnt += 1
        except:
            pass
    return cnt

# 3개인 cnt 개수
result = 0
for i in range(n):
    for j in range(n):
        if count1(i,j) >= 3:
            result += 1
    
print(result)