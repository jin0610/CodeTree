K, N = map(int, input().split())

numbers = []
def backtracking(depth, cnt):
    if depth == cnt:
        print(*numbers)
        return

    for i in range(1, K + 1):
        if (len(numbers) >= 2 and numbers[-2] == i and numbers[-1] == i) :
            continue
        numbers.append(i)
        backtracking(depth, cnt + 1)
        numbers.pop()

    return

backtracking(N, 0)