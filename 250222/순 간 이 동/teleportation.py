# 최선의 가짓수 따지기 / 순간이동
A, B, x, y = map(int, input().split())

dist1 = abs(B - A)                       # A -> B로 간 거리
dist2 = abs(A - x) + abs(B - y)     # A -> x -순간이동- y -> B
dist3 = abs(A - y) + abs(B - x)     # A -> y -순간이동- x -> B
print(min(dist1, dist2, dist3))


    


