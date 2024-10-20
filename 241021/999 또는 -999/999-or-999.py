nums = list(map(int,input().split()))

min_num = 999
max_num = -999

for num in nums:
    if(num == 999 or num == -999):
        break
    elif(min_num > num):
        min_num = num
    elif(max_num < num):
        max_num = num
    
print(max_num, min_num)