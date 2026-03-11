from sortedcontainers import SortedSet
import sys

n = int(input())
arr = list(map(int, input().split()))
s = SortedSet([0])

length = sys.maxsize
for elem in arr:
    s.add(elem)

    # 오른쪽 간격
    x2 = s.bisect_right(elem)
    if x2 < len(s):
        x1 = x2 - 1
        length = min(length, s[x2] - s[x1])

    # 왼쪽 간격
    x2 = s.bisect_left(elem)
    if x2 > 0:
        x1 = x2 - 1
        length = min(length, s[x2] - s[x1])

    print(length)
    