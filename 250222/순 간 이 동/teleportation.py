# 최선의 가짓수 따지기 / 순간이동
A, B, x, y = map(int, input().split())

A, B = min(A, B), max(A, B)         # 0 <= A <= B <= 100로 만들기
x, y = min(x, y), max(x, y)         # 0 <= x <= y <= 100로 만들기

dist1 = B - A                       # A -> B로 간 거리
dist2 = abs(A - x) + abs(B - y)     # A -> x -순간이동- y -> B

print(min(dist1, dist2))


    


