N = int(input())

nums = list(map(int, input().split()))

nums_sorted = sorted(nums, reverse=True)
for i in range(2):
    print(nums_sorted[i], end=" ")