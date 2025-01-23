### 물체 단위로 완전탐색 / 스승의 은혜 3
N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]

# Write your code here!
max_cnt = 0
for i in range(N):
    temp = gifts.copy()

    temp[i][0] /= 2

    prices = [(temp[k][0] +temp[k][1] ) for k in range(N)]
    prices.sort()
    
    student = 0 
    price = 0

    for j in range(N):
        if price + prices[j] > B:
            break
        price += prices[j]
        student += 1
    max_cnt = max(max_cnt, student)

print(max_cnt)
