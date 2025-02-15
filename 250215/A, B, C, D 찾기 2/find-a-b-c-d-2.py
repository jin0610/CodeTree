### 완전탐색 / A, B, C, D 찾기 2
nums = list(map(int, input().split()))

# Write your code here!
nums = sorted(nums)
a, b = nums[0], nums[1]

if (a + b != nums[2]):
    c = nums[2]
else:
    c = nums[3]

d = nums[-1] - a - b - c
print(a, b, c, d)