n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
selected = []
answer = 0

def xor():
    global selected, A

    if len(A) == 1:
        return A[0]

    xor = 1
    for s in selected:
        xor ^= A[s]
    
    return xor

def backtracking(curr_n, cnt):
    global selected, n, m, answer

    if curr_n == m +1:
        answer = max(answer, xor())
        return

    for i in range(n):
        selected.append(i)
        backtracking(curr_n + 1, cnt + 1)
        selected.pop()

        backtracking(curr_n + 1, cnt)


backtracking(1, 0)
print(answer)