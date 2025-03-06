### Ad-hoc (고려해야할 대상이 뚜렷해지는 경우) / 전부 포함하는 선분
import sys
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# x1이 가장 작은 선분만 제거했을 때의 길이
points = sorted(points, key=lambda x:x[0])

min_x, max_x = 101, 0
for i in range(1, n):
    x1, x2 = points[i]
    min_x = min(min_x, x1)
    max_x = max(max_x, x2)

dist = max_x - min_x

# x2가 가장 큰 선분만 제거했을 때의 길이        
points = sorted(points, key=lambda x:x[1])

min_x, max_x = 101, 0
for i in range(n-1):
    x1, x2 = points[i]
    min_x = min(min_x, x1)
    max_x = max(max_x, x2)

dist = min(dist, max_x - min_x)

print(dist)



