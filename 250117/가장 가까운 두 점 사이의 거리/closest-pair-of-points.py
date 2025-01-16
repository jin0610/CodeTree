### 가장 가까운 두 점 사이의 거리
import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
min_dist = sys.maxsize
for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        min_dist = min(min_dist, dist)

print(min_dist)