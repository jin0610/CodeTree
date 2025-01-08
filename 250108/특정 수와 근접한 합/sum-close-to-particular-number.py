### 자리수 단위로 완전 탐색 / 특정 수와 근접한 합
import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

diff = sys.maxsize
hap = sum(arr)
for i in range(N - 1):
    for j in range(i + 1, N):
        num = hap - (arr[i] + arr[j])
        diff = min(diff, abs(S-num))
print(diff)