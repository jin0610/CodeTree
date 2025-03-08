### 완전탐색 3 (기준을 새로 설정하여 완전탐색) / 최대 최소간의 차
import sys

N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 처음부터 최대 최소가 K 이하면 
if max(nums) - min(nums) <= K:
    print(0)
    sys.exit(0)


_min, _max = min(nums), max(nums)
min_cost = sys.maxsize
for p in range(_min, _max + 1):
    cost = 0
    for num in nums:
        if p <= num and num <= p + K:
            continue
        elif num < p:
            cost += p - num
        else:
            cost -= p - num

    min_cost = min(min_cost, cost)

print(min_cost)
            


