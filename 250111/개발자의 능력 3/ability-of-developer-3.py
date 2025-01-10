### 자리마다 숫자를 정하는 완전탐색 / 개발자의 능력 3
import sys
abilities = list(map(int, input().split()))

# Write your code here!
min_diff = sys.maxsize
sum_abilities = sum(abilities)
for i in range(4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            num = abilities[i] + abilities[j] + abilities[k]
            num2 = sum_abilities - num
            min_diff = min(min_diff, abs(num-num2))

print(min_diff)