N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i,N):
        for k in range(j,N):
            if A[i] < A[j] < A[k]:
                cnt += 1
print(cnt)