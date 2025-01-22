### 물체 단위로 완전탐색 / 이상한폭탄 2
N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write your code here!

result = -1
bomb = []
for i in range(N-1):
    for j in range(i+1, N):
        if num[i] == num[j] and abs(i - j) <= K:
            bomb.append(num[i])
            result = max(bomb)        
print(result)