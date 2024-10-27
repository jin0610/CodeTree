n = int(input())

Max_Range = 100000
color = [0] * 2 * Max_Range
start = Max_Range

for _ in range(n):
    dist, direct = input().split()
    dist = int(dist)

    if direct == "L": # white : 1
        for i in range(0, dist):
            color[start - i] = 1
        start -= (dist - 1)
    else: # black : 2
        for i in range(0, dist):
            color[start + i] = 2
        start += (dist - 1)

w, b = 0, 0
for c in color:
    if c == 1:
        w += 1
    elif c == 2:
        b+=1
    else:
        pass
print(w, b)