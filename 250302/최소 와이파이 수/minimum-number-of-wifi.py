### Ad-hoc (지극히 최선인 전략히 확실해진 경우) / 최소 와이파이 수
import sys
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# m이 0인 경우 0 출력
if m == 0:
    print(0)
    sys.exit(0)

# 와이파이를 사용 가능한 거리
use_dist = 2 * m + 1

# n이 use_dist보다 작거나 같은 경우
if n <= use_dist:
    print(1)
    sys.exit(0)

# n이 use_dist보다 작거나 같은 경우
idx = arr.index(1)
cnt = 0
while True:
    idx += use_dist
    cnt += 1

    if idx >= n:
        break

    if arr[idx] == 0:
        idx += 1

    
print(cnt)