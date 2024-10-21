nums = list(map(int, input().split()))

under_500_max = 0
upper_500_min =  1001

for num in nums:
    if(num < 500 and num > under_500_max):
        under_500_max = num
    
    if(num > 500 and num < upper_500_min):
        upper_500_min = num

print(under_500_max, upper_500_min)