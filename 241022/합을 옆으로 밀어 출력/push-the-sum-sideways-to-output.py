n = int(input())

nums = [int(input()) for _ in range(n)]

nums = sum(nums)

result = str(nums)

result = result[1:] + result[0]

print(result)