### 자리마다 숫자를 정하는 완전탐색 / 두 가지로 열리는 자물쇠
import sys
N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Write your code here!
cnt1 = [0,0,0]  # 첫 번쩨 조합의 수
cnt2 = [0,0,0]  # 두 번쩨 조합의 수
cnt3 = [0,0,0]  # 중복된 조합의 수

def is_in_range(N, i, x):
    if abs(i-x) <= 2 or abs(i-x) >= N-2:
        return True
    return False

for i in range(1, N + 1):
    if is_in_range(N, i, a1):
        cnt1[0] += 1
    if is_in_range(N, i, b1):
        cnt1[1] += 1
    if is_in_range(N, i, c1):
        cnt1[2] += 1

    if is_in_range(N, i, a2):
        cnt2[0] += 1
    if is_in_range(N, i, b2):
        cnt2[1] += 1
    if is_in_range(N, i, c2):
        cnt2[2] += 1

    if is_in_range(N, i, a1) and is_in_range(N, i, a2):
        cnt3[0] += 1
    if is_in_range(N, i, b1) and is_in_range(N, i, b2):
        cnt3[1] += 1
    if is_in_range(N, i, c1) and is_in_range(N, i, c2):
        cnt3[2] += 1

comb1, comb2, comb3 = 1,1,1
for i in range(3):
    comb1 *= cnt1[i]
    comb2 *= cnt2[i]
    comb3 *= cnt3[i]

print(comb1 + comb2 - comb3)

