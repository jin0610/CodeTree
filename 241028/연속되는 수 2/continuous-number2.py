N =int(input())

nums = [ int(input()) for _ in range(N)]
max_cnt = 0
cnt = 1
for n in range(1, N):
    if nums[n] == nums[n-1]:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)


print(max_cnt)