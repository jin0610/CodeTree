### 중첩 완전탐색 / 숫자 2배 후 하나 제거하기
import sys
N = int(input())
num_list = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        new_list = num_list.copy()
        new_list[i] *= 2
        new_list.pop(j)
        diff = 0
        for n in range(len(new_list) - 1):
            diff += abs(new_list[n] - new_list[n + 1])

        min_diff = min(min_diff, diff)

print(min_diff)

        