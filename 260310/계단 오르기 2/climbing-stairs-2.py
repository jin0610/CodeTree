n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
dp = [[0 for i in range(4)] for _ in range(n + 1)]

# i번째 계단을 오르는 동안 1계단을 j번 오름
dp[1][1] = coin[1]  
if n > 1:
    dp[2][0] = coin[2]              # 1계단 오르는 것을 한 번 했을 경우
    dp[2][2] = coin[1] + coin[2]    # 1계단 오르는 것을 두 번 했을 경우

for i in range(n + 1):
    for j in range(4):
        # 2계단
        if dp[i-2][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i])
        
        # 1계단
        if j != 0 and dp[i-1][j-1] != 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin[i])


print(max(dp[n]))