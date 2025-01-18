### 물체 단위로 완전탐색 / 삼각형 만들기
import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
max_area = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j +1 ,n):
            # if i != j and j != k and k != i:
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]

            if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
                S = abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))
                max_area = max(S, max_area)
print(max_area)