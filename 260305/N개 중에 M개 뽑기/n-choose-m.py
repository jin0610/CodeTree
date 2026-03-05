N, M = map(int, input().split())

# Please write your code here.
selected = []

def backtracking(curr_n, cnt):
    if curr_n == M:
        print(*selected)
        return 

    for i in range(1, N + 1):
        if cnt < i:
            selected.append(i)
            backtracking(curr_n + 1, i)
            selected.pop()

backtracking(0, 0)