### 완전탐색1 / 마라톤 중간에 택시타기2
import sys

N = int(input())
points = [ input().split() for _ in range(N)]

result = sys.maxsize

for i in range(1, N-1):
    distance = 0
    prev_idx = 0
    
    for j in range(1,N):
        if j == i:
            continue
        
        x1, y1 = map(int,points[prev_idx])
        x2, y2 = map(int,points[j])
        distance += (abs(x1 - x2) + abs(y1- y2))
        prev_idx = j
    
    result = min(result, distance)
print(result)