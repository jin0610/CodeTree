nums = [list(map(int, input().split())) for _ in range(4)]

_sum = 0
for i in range(4):
    for j in range(i+1):
        _sum += nums[i][j]

print(_sum)