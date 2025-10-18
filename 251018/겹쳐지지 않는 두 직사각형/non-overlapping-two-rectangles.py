import sys

N, M = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 사각형의 합 구하기
def get_rect_sum(rect):
    x1, y1, x2, y2 = rect
    num = 0
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            num += grid[i][j]
    return num

# 두 사각형의 교차 여부 확인
def is_intersect(rect1, rect2):
    x1, y1, x2, y2 = rect1
    a1, b1, a2, b2 = rect2

    if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:
        return False
    
    return True

rect_list = []
max_sum = -sys.maxsize

for n in range(N):
    for m in range(M):
        for i in range(n, N):
            for j in range(m, M):
                # x1, y1, x2, y2
                rect_list.append([m, n, j, i])  
              

for rect1 in rect_list:
    for rect2 in rect_list:
        if is_intersect(rect1, rect2) or rect1 == rect2:
            continue
        num = get_rect_sum(rect1) + get_rect_sum(rect2)
        max_sum = max(max_sum, num)

print(max_sum)