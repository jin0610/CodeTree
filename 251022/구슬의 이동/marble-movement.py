n, m, t, k = map(int, input().split())

directions = {'U':0, 'R':1, 'D':2, 'L':3}
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

marbles = []

for i in range(m):
    r, c, d, v = input().split()
    r, c, d, v = int(r) - 1, int(c) - 1, directions[d], int(v)
    marbles.append((i + 1, r, c, d, v))

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

def move_marble(marble):
    idx, r, c, d, v = marble
    for _ in range(v):
        nr, nc = r + drs[d], c + dcs[d]
        if not in_range(nr,nc):
            d = (d + 2) % 4
            nr, nc = r + drs[d], c + dcs[d]
        r, c = nr, nc
    return (idx, nr, nc, d, v)

def move(marble_position):
    new_position = {}
    for marble in marble_position:
        new_marble = move_marble(marble)
        idx, r, c, d, v = new_marble
        if (r, c) not in new_position.keys():
            new_position[(r, c)] = [(idx, d, v)]
        else:
            new_position[(r, c)].append((idx, d, v))

    new_marbles = []
    for key, values in new_position.items():
        r, c = key
        if len(values)> k:
            values.sort(key = lambda x:(-x[2], -x[0]))
            for value in values[:k]:
                i, d, v = value
                new_marbles.append((i, r, c, d, v))
        else:
            for value in values:
                i, d, v = value
                new_marbles.append((i, r, c, d, v))
    return new_marbles

for _ in range(t):
    marbles = move(marbles)

print(len(marbles))