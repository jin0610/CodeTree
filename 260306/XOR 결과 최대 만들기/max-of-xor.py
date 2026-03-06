n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
selected = []
answer = 0

def xor():
    xor = 1
    for s in selected:
        xor ^= A[s]
    return xor

def backtracking(curr_n, num):
    global answer, m, n, selected
    if curr_n == m:
        answer = max(answer, xor())
        return

    for i in range(n):
        if num < i:
            selected.append(i)
            backtracking(curr_n + 1, i)
            selected.pop()

backtracking(1, 0)
print(answer)