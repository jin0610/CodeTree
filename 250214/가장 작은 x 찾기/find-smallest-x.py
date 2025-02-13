import sys
n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]


# Write your code here!
def in_range(x):
    for i in range(n):
        if 2 * x >= ranges[i][0] and 2 * x <= ranges[i][1]:
            x = 2 * x
        else:
            return False
    return True

num = []
for i in range(ranges[0][0], ranges[0][1] + 1):
    if in_range(i):
        num.append(i)

print(min(num))
        