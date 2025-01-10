### 구간단위로 완전탐색 / 밭의 높이를 고르게 하기
import sys
N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
result = sys.maxsize
for i in range(N - T + 1):
    price = abs(H - arr[i])
    for j in range(i + 1, i + T):
        price += abs(H - arr[j])
    
    result = min(result, price)

print(result)
