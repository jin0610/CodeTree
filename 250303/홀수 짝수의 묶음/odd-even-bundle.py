import sys
N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
odds = 0
pairs = 0

for i in range(N):
    if numbers[i] % 2== 0:
        pairs += 1
    else:
        odds += 1

# Case 1. 짝수만 있을 경우 조합은 무조건 1개
if odds == 0:
    print(1)
    sys.exit(0)

# Case 2. 짝수와 홀수의 개수가 같을 경우
if pairs == odds:
    print(2 * pairs)
    sys.exit(0)
# Case 3. 짝수가 홀수의 개수보다 많을 경우 
elif pairs > odds:
    print(2 * odds + 1)
    sys.exit(0)
# Case 4. 홀수가 짝수의 개수보다 많을 경우
else:
    comb = 2 * pairs
    remain_odds = odds - pairs

    if (remain_odds % 3) == 0:
        comb += remain_odds // 3 * 2
    else:
        if (remain_odds % 3) % 2 == 0:
            comb += remain_odds // 3 * 2 + 1
        else:
            comb += remain_odds // 3 * 2 - 1

print(comb)




