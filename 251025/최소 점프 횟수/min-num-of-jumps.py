import sys

_MAX = sys.maxsize

# 변수 입력
n = int(input())
nums = list(map(int, input().split()))

answer = _MAX

def backtracking(idx, cnt):
    global answer

    if idx >= n - 1:
        answer = min(answer, cnt)
        return

    for dist in range(1, num[idx] + 1):
        backtriking(idx + dist, cnt + 1)

backtracking(0, 0)

if answer = _MAX:
    answer = -1

print(answer)