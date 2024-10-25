class Point:
    def __init__(self, idx,x, y, distance):
        self.idx = idx
        self.x = x
        self.y = y
        self.distance = distance

N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    dist = abs(x - 0) + abs(y - 0)

    points.append(Point(i + 1, x, y, dist))

points.sort(lambda x : (x.distance, x.idx))

for i in points:
    print(i.idx)