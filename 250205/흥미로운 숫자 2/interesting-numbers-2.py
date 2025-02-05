# 값을 기준으로 완전 탐색 / 흥미로운 숫자 2
X, Y = map(int, input().split())

# Write your code here!
# 흥미로운 숫자 : 모든 자릿수에 있는 숫자들이 같지만, 정확히 한 자리만 다른 숫자
# 조건 1 : 흥미로운 숫자는 각 자리가 두가지의 숫자로 이루어짐
# 조건 2 : 흥미로운 숫자를 이루는 두 가지의 숫자 중 하나는 1개만 있음
result = 0
for num in range(X, Y+1):
    # 각 자리의 숫자를 리스트에 저장
    num_list = list(map(int, str(num)))

    # 조건 1 
    if len(set(num_list)) == 2:
        number = list(set(num_list))
        # 조건2
        if num_list.count(number[0]) == 1 or num_list.count(number[1]) == 1:
            result += 1

print(result)
