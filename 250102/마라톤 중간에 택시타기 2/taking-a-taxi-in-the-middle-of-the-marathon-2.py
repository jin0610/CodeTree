### 완전탐색1 / 마라톤 중간에 택시타기2
import sys

N = int(input())
points = [ input().split() for _ in range(N)]

result = sys.maxsize

for i in range(1, N-1):
    point = points.copy()
    length = 0
    point.pop(i)

    for j in range(1,len(point)):
        x1, y1 = map(int,point[j-1])
        x2, y2 = map(int,point[j])
        length = length + (abs(x1 - x2) + abs(y1- y2))
    
    result = min(result, length)
print(result)