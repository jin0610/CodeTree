### 값을 기준으로 완전탐색 / 팰린드롬 수 찾기
X, Y = map(int, input().split())

# Write your code here!
# 방법 2 리스트를 거꾸로 바꿔서 한 풀이
result = 0
for num in range(X, Y + 1):
    str_num = str(num)
    if str_num == str_num[::-1]:
        result += 1

print(result)

# 방법 1 리스트를 모두 탐색하는 풀이
# def isPalindrome(n):
#     num_list = list(str(n))
#     num_len = len(num_list)
#     for i in range(num_len // 2):
#         if num_list[i] != num_list[num_len-i-1]:
#             return False
#     return True

# result = 0
# for num in range(X, Y + 1):
#     if isPalindrome(num):
#         result += 1

# print(result)
