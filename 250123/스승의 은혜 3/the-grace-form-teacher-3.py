### 물체 단위로 완전탐색 / 스승의 은혜 3
N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
gifts = sorted(gifts, key= lambda x : (x[0]//2 + x[1]))

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
        cnt += 1
        if money < 0:  
            cnt -= 1
            break
        
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
