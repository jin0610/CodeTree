import sys
n, t = map(int, input().split())
nums = list(map(int, input().split()))

result, cnt = 0,0
for i in range(n):
    if nums[i] > t:
        cnt += 1
    else:
        cnt = 0
    result = max(result, cnt)

print(result)