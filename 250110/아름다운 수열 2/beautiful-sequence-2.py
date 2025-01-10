### 구간 단위로 완전탐색 / 아름다운 수열2
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = sorted(B)
result=0
for n in range(N-M+1):
    if sorted(A[n:n+M]) == B:
        result +=1

print(result)