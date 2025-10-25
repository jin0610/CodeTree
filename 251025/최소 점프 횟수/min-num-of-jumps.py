# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# 계산1: 초기화
dp = [-1 for _ in range(n)]
dp[0] = 0

# 계산2: dp
for i in range(n-1):
    for k in range(arr[i]):

        if (i + (k+1)) < n:
            if dp[i + (k+1)] == -1:
                dp[i + (k+1)] = dp[i] + 1
            else:
                dp[i + (k+1)] = min(dp[i + (k+1)], dp[i] + 1)

# 출력
print(dp[-1])
