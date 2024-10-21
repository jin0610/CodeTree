n = int(input())

maps = []
num = 1

for i in range(n):
    nums=[]
    for j in range(n):
        nums.append(num)
        num = num + 1
    maps.append(nums)


maps = list(zip(*maps))
for i in range(n):
    print(*maps[i])