N = int(input())

nums = list(map(int, input().split()))

nums.sort()

result = 0
for n in range(N):
    num = nums[n] + nums[2*N - 1 - n]
    if result < num:
        result = num

print(num)