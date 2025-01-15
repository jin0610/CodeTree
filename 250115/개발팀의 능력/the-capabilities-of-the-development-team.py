### 자리마다 숫자를 정하는 완전탐색 / 개발팀의 능력
import sys
arr = list(map(int, input().split()))

# Write your code here!
total_ability = sum(arr)
ability_sum = [0] * 3
min_diff = 1000
for i in range(5):
    for j in range(5):
        for k in range(j + 1, 5):
            if i == j or i == k:
                continue
            ability_sum[0] = arr[i]
            ability_sum[1] = arr[j] + arr[k]
            ability_sum[2] = total_ability - ability_sum[0] - ability_sum[1]
            if len(set(ability_sum)) == 3:
                min_diff = min(min_diff, max(ability_sum) - min(ability_sum))
            
if min_diff == 1000:
    print(-1)
else:
    print(min_diff)

