### 완전 탐색 / 수들의 최대 차
N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Write your code here!
answer = 0
arr = sorted(arr)
for i in range(N - 1):
    temp = []
    temp.append(arr[i])
    for j in range(i + 1, N):
        if abs(arr[j] - arr[i]) <= K:
            temp.append(arr[j])

    answer = max(answer, len(temp))

print(answer)