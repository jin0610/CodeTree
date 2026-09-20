N = int(input())

nums = dict()

for n in range(N):
    order = input().split()
    if order[0] == 'add':
        nums[order[1]] = order[2]
    elif order[0] == 'remove':
        nums.pop(order[1])
    else:
        if order[1] in nums.keys():
            print(nums[order[1]])
        else:
            print(None)