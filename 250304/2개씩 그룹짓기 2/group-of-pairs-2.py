### Ad-hoc (지극히 최선인 전략이 정해진 경우) / 2개씩 그룹짓기 2
import sys

n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

answer = sys.maxsize
for i in range(n):
    diff = arr[i + n] - arr[i]
    answer = min(answer, diff)

print(answer)