n = int(input())

nums = list(map(int, input().split()))

idx = nums.index(max(nums))
max_idx = [idx+1]

while idx != 0:
    nums = nums[:idx]
    idx = nums.index(max(nums))
    max_idx.append(idx+1)

print(*max_idx)