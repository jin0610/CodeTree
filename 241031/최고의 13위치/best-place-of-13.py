N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_cnt = -1
for i in range(N):
    for j in range(N-2):
        cnt = arr[i][j : j + 3].count(1)
        
        max_cnt = max(max_cnt, cnt)

print(max_cnt)