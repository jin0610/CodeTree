n = int(input())

location = [0] * 200
start = 100

for _ in range(n):
    dist, direct = input().split()
    dist = int(dist)

    # print(_, start, direct, dist)
    if direct == "R":
        for i in range(1, dist + 1):
            location[start + i] += 1
        start += dist
    else:
        for i in range(1, dist + 1):
            location[start - i] += 1
        start -= dist

cnt = 0
for l in location:
    if l >= 2:
        cnt += 1
print(cnt)