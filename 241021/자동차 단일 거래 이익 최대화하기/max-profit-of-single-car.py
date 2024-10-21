n = int(input())

prices = list(map(int, input().split()))

profit = 0
left, right = 0, len(prices)

for i in range(n-1):
    for j in range(i, n):
        if(prices[i] > prices[j]):
            pass
        else:
            if(profit < prices[j]-prices[i]):
                profit = prices[j]-prices[i]

print(profit)