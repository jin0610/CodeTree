N = int(input())
arr = []

for _ in range(N):
    nums = list(map(int,input().split(' ')))
    arr.append(nums)

coins = 0
for i in range(N-2):
    for j in range(N-2):
        cnt = 0
        for a in range(i, i + 3):
            for b in range(j, j + 3):
               cnt = cnt + arr[a][b] 

        coins = max(coins, cnt)

print(coins)

