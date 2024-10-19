n = int(input())

nums = list(map(int, input().split()))

for num in nums:
    if(num % 2 == 0):
        print(num, end = " ")