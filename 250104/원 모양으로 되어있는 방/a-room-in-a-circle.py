### 자리 수 단위로 완전탐색 / 원 모양으로 되어있는 방
import sys

n = int(input())
rooms = [int(input()) for _ in range(n)]

result = sys.maxsize

for i in range(n):
    distance = 0

    for j in range(n):
        if (j - i) >= 0:
            moved = abs(i - j)
        else:
            moved = n - abs(i - j)
        distance += (moved * rooms[j])

    result = min(result, distance) 

print(result)