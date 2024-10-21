N,M = list(map(int, input().split()))

result = [[0 for _ in range(M)] for _ in range(N)]

num = 0
for m in range(M):
    for n in range(N):
        if m % 2 == 1:
            result[N-n-1][m]=num
        else:
            result[n][m] = num
            
        num = num + 1

for i in range(N):
    print(*result[i])