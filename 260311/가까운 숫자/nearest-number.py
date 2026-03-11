from sortedcontainers import SortedSet
import sys

n = int(input())
arr = list(map(int, input().split()))

s = SortedSet()
s.add(0)

length = sys.maxsize
for elem in arr:
    s.add(elem)
    x2 = s.bisect_right(elem)
    if x2 >= len(s):
        x2 = len(s) - 1
        
    x1 = x2 - 1
    length = min(length, s[x2] - s[x1])
    print(length)
