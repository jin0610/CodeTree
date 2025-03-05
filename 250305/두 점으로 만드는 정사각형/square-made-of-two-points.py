### Ad-hoc (고려해야할 대상이 뚜렷해지는 경우) / 두 점으로 만드는 정사각형
x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# 밑변 : 가장 큰 x좌표에서 가장 작은 x좌표를 뺌
width = max(a2, x2) - min(x1, a1)

# 높이 : 가장 큰 y좌표에서 가장 작은 y좌표를 뺌
height = max(y2,b2) - min(y1, b1)

# 밑변과 높이 중 긴 변을 선택
print(max(width, height) ** 2)