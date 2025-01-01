### 자리 수 단위로 완전탐색 / 이상한 진수2

import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
binary = list(map(int, list(input())))
length = len(binary)

# 각 i번째 자릿수를 바꾸었을 때의 십진수 값을 구해줍니다.
ans = INT_MIN
for i in range(length):
	# i번째 자릿수를 바꿉니다.
	binary[i] = 1 - binary[i]
	
	# 십진수로 변환합니다.
	num = 0
	for j in range(length):
		num = num * 2 + binary[j]
	
	ans = max(ans, num)
	
	# i번째 자릿수를 원래대로 돌려놓습니다.
	binary[i] = 1 - binary[i]

# 출력
print(ans)

# a = input()

# result = -1

# for i in range(len(a)):

#     ## if문을 사용하지 않은 풀이 44ms
#     num = a[:i] + str(1 - int(a[i])) + a[i+1:]

#     ## if문을 사용하는 풀이 43ms
#     # if a[i] == '1':
#     #     num = a[:i] + '0' + a[i+1:]
#     # else:
#     #     num = a[:i] + '1' + a[i+1:]

#     result = max(result, int(num,2))  

# print(result)
        
