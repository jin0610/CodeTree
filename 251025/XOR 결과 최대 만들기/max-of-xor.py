N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
def find_max_num(idx, curr_num, cnt):
    global answer

    if cnt >= M:
        answer = max(answer, curr_num)
        return

    for i in range(idx, N):
        find_max_num(i + 1, curr_num ^ arr[i], cnt + 1)

    return

find_max_num(0, 0, 0)
print(answer)