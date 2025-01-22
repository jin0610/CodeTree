### 물체 단위로 완전탐색 / 이상한폭탄 2
N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write your code here!
result = -1
for i in range(N-1):
    for j in range(i+1, N):
        if num[i] == num[j] and abs(i - j) <= K:
            result = max(result, num[i])        
print(result)