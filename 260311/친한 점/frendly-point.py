from sortedcontainers import SortedSet
n, m = map(int, input().split()) # n 개의 점 m개의 질의

# Store points as list of tuples
points = SortedSet()
for _ in range(n):
    p = tuple(map(int, input().split()))
    points.add(p)

for _ in range(m):
    p = tuple(map(int, input().split()))
    idx = points.bisect_right(p)
    if idx == len(points):
        print("-1 -1")
    else:
        print(*points[idx])