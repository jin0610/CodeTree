n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
result = 0

def diff(k, n, nums):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] == k or nums[j] == k:
                continue
            if abs(nums[i] - k) == abs(nums[j] - k):
                cnt += 1
    return cnt


for k in range(1, max(nums) + 1):
    result = max(result, diff(k, n, nums))

print(result)