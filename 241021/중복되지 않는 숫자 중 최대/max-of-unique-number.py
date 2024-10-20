N = int(input())

nums = list(map(int, input().split()))

nums2=[]

for num in nums:
    if(nums.count(num) >= 2):
        pass
    else:
        nums2.append(num)

if(len(nums2)>0):
    print(max(nums2))
else:
    print(-1)