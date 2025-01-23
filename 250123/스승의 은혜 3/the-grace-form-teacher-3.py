### 물체 단위로 완전탐색 / 스승의 은혜 3
N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]
gifts = sorted(gifts, key= lambda x : (x[0]//2 + x[1]))

# Write your code here!
max_cnt = 0
for i in range(N):
    money = B
    p, s = gifts[i]
    p = p // 2
    money -= (p + s)
    cnt = 1
    for j in range(N):
        if i == j:
            continue        
        if money - sum(gifts[j]) < 0:  
            break
        cnt += 1
        money -= sum(gifts[j])
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
