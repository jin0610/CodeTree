### 값을 기준으로 완전탐색 / 팰린드롬 수 찾기
X, Y = map(int, input().split())

# Write your code here!
def isPalindrome(n):
    num_list = list(str(n))
    num_len = len(num_list)
    for i in range(num_len // 2):
        if num_list[i] != num_list[num_len-i-1]:
            return False
    return True

result = 0
for num in range(X, Y + 1):
    if isPalindrome(num):
        result += 1

print(result)
