import sys

N = int(input())
nums = list(map(int, input().split()))

INT_MAX = sys.maxsize
answer = INT_MAX

def get_min_jump(idx, cnt):
    global answer

    if idx >= N - 1:
        answer = min(answer, cnt)
        return

    for dist in range(1, nums[idx] + 1):
        get_min_jump(idx + dist, cnt + 1)

    return

get_min_jump(0, 0)
if answer == INT_MAX:
    print(-1)
else:
    print(answer)  
