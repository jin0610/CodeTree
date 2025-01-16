### 물체 단위로 완전탐색 / 
import sys

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
min_rect = sys.maxsize
for i in range(N):
    x1, y1 = sys.maxsize, sys.maxsize
    x2, y2 = -sys.maxsize, -sys.maxsize
    for j in range(N):
        if i != j:
            x1, y1 = min(x1, x[j]), min(y1, y[j])
            x2, y2 = max(x2, x[j]), max(y2, y[j])

    rect = abs(x2 - x1) * abs(y2 - y1)
    min_rect = min(min_rect, rect)

print(min_rect)