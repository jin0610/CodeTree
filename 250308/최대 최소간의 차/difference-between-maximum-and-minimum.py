### 완전탐색 3 (기준을 새로 설정하여 완전탐색) / 최대 최소간의 차
import sys

N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 처음부터 최대 최소가 K 이하면 
if max(nums) - min(nums) <= K:
    print(0)
    sys.exit(0)


min_cost = sys.maxsize
for point in range(min(nums), max(nums) + 1):
    cost = 0
    for num in nums:
        if num >= point and num <= point + K:
            continue
        elif num < point:
            cost += abs(point - num)
        else:
            cost += abs(num - (point + K))

    min_cost = min(min_cost, cost)

print(min_cost)
            


