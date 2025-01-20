### 물체 단위로 완전탐색 / 스승의 은혜 2
N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Write your code here!
gift_cnt = 0

for i in range(N):
    money = B
    cnt = 0
    for j in range(N):
        if i == j:
            price = P[j] // 2
            money -= price
        else:
            money -= P[j]
        if money >= 0:
            cnt +=1
        else:
            break
    gift_cnt = max(gift_cnt, cnt)


print(gift_cnt)