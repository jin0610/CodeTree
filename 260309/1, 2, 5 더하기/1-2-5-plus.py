n = int(input())

# Please write your code here.
nums = [1, 2, 5]
selected = []
answer =0
def backtracking(curr_n,cnt):
    global nums, selected, answer 

    if curr_n == cnt:
        if sum(selected) == n:
            answer +=1
        return

    for num in nums:
        selected.append(num)
        backtracking(curr_n + 1, cnt)
        selected.pop()

for i in range(min(nums), n//min(nums) +1):
    backtracking(0,i)

print(answer)

'''

dp = [0 for _ in range(n + 1)]
dp[1] = 1
for num in nums:
    for j in range(1, n + 1):
        if dp[j - num] != 0:
            dp[j] += 1

print(dp)
print(dp[-1] % 10007)
'''