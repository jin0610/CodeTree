import sys
# 입력
N, M = map(int, input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(N)
]

# 행복한 수열 찾기
result = 0

if N == 1 and M == 1:
    print(2)
    sys.exit(0)

# 열
for i in range(N):
    cnt = 1
    for j in range(N-1):
        if arr[i][j] == arr[i][j+1]:
            cnt = cnt + 1
        else:
            cnt = 1

        if cnt >= M:
            result = result + 1
            break

        

# 행
for i in range(N):
    cnt = 1
    for j in range(N-1):
        if arr[j][i] == arr[j+1][i]:
            cnt = cnt + 1
        else:
            cnt = 1

        if cnt >= M:
            result = result + 1
            break
print(result)