K, N = map(int, input().split())

# Please write your code here.
selected_nums = []

def backtracking(curr_n):
    global K, N, selected_nums

    if curr_n == N:
        print(*selected_nums)
        return

    for i in range(1, K + 1):
        if len(selected_nums) >= 2 and selected_nums[curr_n-1] == i and selected_nums[curr_n-2] == i:
            continue

        selected_nums.append(i)
        backtracking(curr_n + 1)
        selected_nums.pop()

backtracking(0)