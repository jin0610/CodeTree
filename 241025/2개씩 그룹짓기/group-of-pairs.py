N = int(input())

nums = list(map(int, input().split()))

nums.sort()

arr = []
for n in range(N):
    num = nums[n] + nums[2*N - 1 - n]
    arr.append(num)

print(max(arr))