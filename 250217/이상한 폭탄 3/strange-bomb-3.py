N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write your code here!

bomb_num = sorted(list(set(num)))
max_bomb = 0
max_cnt = 0

for bomb in bomb_num:
    pre_idx = num.index(bomb)
    cnt = 0
    for j in range(pre_idx + 1, N):
        if num[j] == bomb and (j - pre_idx) <= K:
            cnt += 1

    if cnt >= max_cnt:
        max_bomb = bomb
        max_cnt = cnt

if max_cnt == 0:
    print(0)
else:
    print(max_bomb)
