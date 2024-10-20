nums = list(map(int,input().split()))

min_num = 0
max_num = 0

for num in nums:
    if(num == 999 or num == -999):
        break
    else:
        if(min_num > num):
            min_num = num

        if(max_num < num):
            max_num = num

print(max_num, min_num)