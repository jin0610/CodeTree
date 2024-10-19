n, q = list(map(int, input().split()))
nums = list(map(int, input().split()))

quests = [list(map(int, input().split())) for i in range(q)]

for quest in quests:
    if(quest[0] == 1):
        print(nums[quest[1]-1])
    elif(quest[0] == 2):
        if(quest[1] in nums):
            print(nums.index(quest[1]) + 1)
        else:
            print(0)
    else:
        for i in range(quest[1]-1, quest[2]):
            print(nums[i], end=" ")