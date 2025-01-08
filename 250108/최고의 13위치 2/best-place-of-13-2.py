### 자리 수 단위로 완전 탐색 / 최고의 13 위치 2
import sys

N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N)] 

result = 0
for i in range(N):
    for j in range(N-2):
        for k in range(N):
            for l in range(N-2):
                if k == i and abs(i-j) <= 2:
                    continue

                cnt1 = sum(arr[i][j:j+3])
                cnt2 = sum(arr[k][l:l+3])
                result = max(result, cnt1 + cnt2)


print(result)
