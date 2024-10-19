n, q = list(map(int, input().split()))
nums = list(map(int, input().split()))

quests = []
for i in range(q):
    quests.append(list(map(int, input().split())))

for quest in quests:
    if(quest[0] == 1):
        idx = quest[1] - 1
        print(nums[idx])
    elif(quest[0]==2):
        if(quest[1] in nums):
            idx = nums.index(quest[1])
            print(idx + 1)
        else:
            print(0)
    else:
        n1 = quest[1]
        n2 = quest[2]
        for i in range(n1-1, n2):
            print(nums[i], end=" ")
        print()