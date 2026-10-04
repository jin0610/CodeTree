n, m = map(int, input().split())
bombs = []

for _ in range(n):
    bombs.append(int(input()))

def get_end_of_idx(start_idx, num):
    for idx in range(start_idx, len(bombs)):
        if bombs[idx] != num:
            return idx - 1
    return len(bombs) - 1

while True:
    explosed = False

    for idx, num in enumerate(bombs):
        end_idx = get_end_of_idx(idx, num)

        if num == 0:
            continue

        if end_idx - idx + 1 >= m:
            bombs[idx:end_idx + 1] = [0] * (end_idx - idx + 1)
            explosed = True

    if explosed:
        bombs = [x for x in bombs if x != 0]
    else:
        break

print(len(bombs))
for i in range(len(bombs)):
    print(bombs[i])