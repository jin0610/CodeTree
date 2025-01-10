### 구간 단위로 완전탐색 / 바구니 안의 사탕2
import sys

N,K = map(int, input().split())
candy_cnt = []
candy_index = []
for _ in range(N):
    c, i = map(int, input().split())    # [각 사탕의 개수, 바구니의 좌표]
    candy_cnt.append(c)
    candy_index.append(i)

if (max(candy_index) // 2) - K < 0:
    print(sum(candy_cnt)) 
    sys.exit(0)
    
candy = [0] * (max(candy_index)+1)

result = 0
for c, i in zip(candy_cnt, candy_index):
    candy[i] += c

for i in range(K, len(candy)-K+1):
    result = max(result, sum(candy[i-K : i+K+1]))

print(result)