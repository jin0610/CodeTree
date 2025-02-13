import sys
n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]


# Write your code here!
def in_range(x):
    for a, b in ranges:
        if 2 * x >= a and 2 * x <= b:
            x = 2 * x
        else:
            return False
    return True

for i in range(0, ranges[0][1] + 1):
    if in_range(i):
        print(i)
        break


        