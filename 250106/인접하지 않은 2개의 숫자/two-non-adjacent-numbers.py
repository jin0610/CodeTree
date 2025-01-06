### 자리수 단위로 완전탐색 / 인접하지 않은 2개의 숫자
import sys
n = int(input())
numbers = list(map(int, input().split()))

# Write your code here!
result = -sys.maxsize
for i in range(n-2):
    for j in range(i+2, n):
        result = max(result, numbers[i]+numbers[j])

print(result)