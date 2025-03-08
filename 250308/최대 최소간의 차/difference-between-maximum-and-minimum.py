### 완전탐색 3 (기준을 새로 설정하여 완전탐색) / 최대 최소간의 차
import sys

N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 처음부터 최대 최소가 K 이하면 
if  <= K:
    print(0)

min_cost = 0

# 차이가 K + 1 이하면 최대값만 -1하기
if max(nums) - min(nums) == K + 1:      
    for i in range(N):
        if nums[i] == _max:
            nums[i] -= 1
            min_cost += 1
    print(min_cost)
    sys.exit(0)

# 최대와 최소 간의 차가 K + 1 이상일 경우
while True:
    _max, _min = max(nums), min(nums)   # 최대 최소 구하기
    diff = _max - _min                  # 최대와 최소 차 구하기

    if diff <= K:                       # 차이가 K 이하면 멈추기
        break

    if diff > K + 1:
        for i in range(N):
            if nums[i] == _max:
                nums[i] -= 1
                min_cost += 1

            elif nums[i] == _min:
                nums[i] += 1
                min_cost += 1

print(min_cost)    