n = int(input())

nums = list(map(int, input().split()))

result = [0]*10

for i in range(n):
    result[nums[i]] += 1

for i in range(1, 10):
    print(result[i])