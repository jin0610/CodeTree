### 완전탐색 / 초기 수열 복원하기
N = int(input())
arr = list(map(int, input().split()))

answer = [0] * N
for i in range(N - 1):
    answer[i] = (i + 1)
    answer[i + 1] = arr[i] - answer[i] 

for i in range(1, N + 1):
    answer[0] = i
    for j in range(N-1):
        answer[j + 1] = arr[j] - answer[j]
        if (answer[j + 1] <= 0) or (answer[j + 1] > N):
            break
    
    if len(set(answer)) == N:
        print(" ".join(map(str,answer)))
        break
    else:
        answer = [0] * N

    
