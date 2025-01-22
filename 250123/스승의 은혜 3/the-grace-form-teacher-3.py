### 물체 단위로 완전탐색 / 스승의 은혜 3
N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Write your code here!
max_cnt = 0
for i in range(N):
    cnt = 0
    money = B
    for j in range(N):
        p, s = gifts[j]
        if i == j:
            p = p // 2
        money -= (p + s)
        if money < 0:
            break
        cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
