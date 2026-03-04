n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
selected = []
answer = 0

def cal_score():
    global nums, selected, m, n

    score = [1] * (n + 1)
    for i in range(n):
        score[selected[i]] += nums[i]

    count = 0
    for i in score:
        if i >= m:
            count += 1
    return count

def backtracking(curr_n):
    global n, m ,k, num, selected, answer

    if curr_n == n:
        answer = max(answer, cal_score())
        return

    for i in range(1, k + 1):
        selected.append(i)
        backtracking(curr_n + 1)
        selected.pop()

backtracking(0)

print(answer)