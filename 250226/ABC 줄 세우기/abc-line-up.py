### 케이스별로 나누기 / ABC 줄 세우기
N = int(input())
alpha = input().split()

idx = 0
cnt = 0
isTrue = 0
while True:
    if idx != N - 1 and (alpha[idx] > alpha[(idx + 1) % N]):
        alpha[idx], alpha[(idx + 1) % N] = alpha[(idx + 1) % N], alpha[idx]
        cnt += 1
        isTrue = 0
        
    idx = (idx + 1) % N
    isTrue += 1

    if isTrue > N:
        break

print(cnt)