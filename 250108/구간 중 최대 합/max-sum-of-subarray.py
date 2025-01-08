### 구간 단위로 완전 탐색 / 구간 중 최대 합
import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
result = -sys.maxsize

for i in range(n-k+1):
    result = max(result, sum(arr[i : i + k]))
print(result)