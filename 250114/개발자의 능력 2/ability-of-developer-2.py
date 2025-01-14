### 자리마다 숫자를 정하는 완전탐색 / 개발자의 능력 2
import sys
ability = list(map(int, input().split()))

# Write your code here!
total_ability = sum(ability)
ability_sum = [0] * 3
min_diff = sys.maxsize
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(6):
            for l in range(k + 1, 6):
                if i != k and i != l and j != k and j != l:
                    ability_sum[0] = ability[i] + ability[j]
                    ability_sum[1] = ability[k] + ability[l]
                    ability_sum[2] = total_ability - ability_sum[0] -ability_sum[1]
                    diff =  max(ability_sum) - min(ability_sum)
                    min_diff = min(min_diff, diff)
print(min_diff)