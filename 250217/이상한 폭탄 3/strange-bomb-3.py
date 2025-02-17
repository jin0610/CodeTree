N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write your code here!

bomb_num = sorted(list(set(num)))
max_bomb = 0
max_cnt = 0

for bomb in bomb_num:
    pre_idx = num.index(bomb)
    cnt = 0
    for j in range(num.index(bomb) + 1, N):
        if num[j] == bomb:
            if (j - pre_idx) <= K:
                cnt += 1
            pre_idx = j
            
    if cnt != 0 and cnt >= max_cnt:
        max_bomb = bomb
        max_cnt = cnt

print(max_bomb)
