N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(N-2):
    for j in range(i + 1, N-1):
        if nums[i] <= nums[j]:
            for k in range(j + 1, N):
                if nums[j] <= nums[k]:
                    cnt += 1
print(cnt)