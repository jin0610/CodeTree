### 구간 단위로 완전탐색 / 특정 구간의 원소 평균값
N = int(input())
arr = list(map(int, input().split()))

result = 0

# 원소가 한 개일 경우
for i in range(N):
    for j in range(i,N):
        mean_num = sum(arr[i : j + 1]) / len(arr[i : j + 1])
        if mean_num in arr[i : j + 1]:
            result +=1

print(result)