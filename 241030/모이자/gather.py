import sys

n = int(input())
arr = list(map(int, input().split()))

min_diffs = []
min_diff = sys.maxsize
for i in range(n):
    dist = 0
    for j in range(n):

        dist = dist + arr[j] * abs(i-j)

    min_diff = min(dist, min_diff)
print(min_diff)