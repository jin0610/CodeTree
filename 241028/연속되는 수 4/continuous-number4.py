import sys

N = int(input())

if N == 1:
    print(1)
    sys.exit(0)

nums = [int(input()) for _ in range(N)]

max_cnt, cnt = 0, 1

for n in range(1, N):
    if nums[n-1] < nums[n]:
        cnt +=1
    else:
        cnt =1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)