N = int(input())
a, b, c = map(int, input().split())

# Write your code here!
# 자물쇠를 열 수 없는 숫자의 개수 찾기
# diff1, diff2, diff3 = 0, 0, 0
# for i in range(1, N + 1):
#     if abs(a - i) > 2:
#         diff1 += 1
#     if abs(b - i) > 2:
#         diff2 += 1
#     if abs(c - i) > 2:
#         diff3 += 1

# # 나올 수 있는 모든 조합의 수
# all_comb = N ** 3

# # 자물쇠를 열 수 없는 조합의 수
# non_comb = diff1 * diff2 * diff3

# print(all_comb - non_comb)


### 완전탐색 방법 ###
cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            # 한자리라도 주어진 조합과의 거리가 2 이내인지 확인
            if abs(a - i) <= 2 or abs(b - j) <= 2 or abs(c - k) <= 2:
                cnt+=1
print(cnt)