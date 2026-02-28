N = int(input()) # N자리의 수

nums = []
answer = 0

def is_beautiful():
    global N, nums

    i = 0
    while i < N:
        if (i + nums[i] - 1) >=  N:
            return False

        for j in range(i, i + nums[i]):
            if nums[i] != nums[j]:
                return False

        i = i + nums[i]

    return True


def backtracking(curr_n):
    global N, nums, answer

    if curr_n == N:
        if is_beautiful():
            answer += 1
        return

    for i in range(1, 5):
        nums.append(i)
        backtracking(curr_n + 1)
        nums.pop()

    
backtracking(0)
print(answer)