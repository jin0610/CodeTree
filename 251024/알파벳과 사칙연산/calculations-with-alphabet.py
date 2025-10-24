from collections import deque
expression = list(input())

alpha = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5
}

def operations():
    global numbers, expression, alpha

    n1 = numbers[alpha[expression[0]]]
    fx = deque([n1])
    for s in expression[1: ]:
        if s in ['-', '*', '+']: # s가 수식기호이면 deque에 넣기
            fx.append(s)
        else:   # s가 숫자이면 계산
            temp_s = fx.pop()       # 사칙연산 기호            
            n1 = fx.pop()           # 첫번째 숫자
            n2 = numbers[alpha[s]]  # 두번째 숫자는 현재 s 

            if temp_s == "-":
                value = n1 - n2
            elif temp_s == "+":
                value = n1 + n2
            else:
                value = n1 * n2
            fx.append(value)        # 값 저장

    result = fx.pop()
    return result
    
numbers = []    # index 0 - a, index 1 - b, index 2 - c, index 3 - d ...
result = -999  # 출력 가능한 최대 결과
def alpha_corr(cnt):
    global numbers, result
    if cnt == 6:
        result = max(result, operations())
        return

    for i in range(1, 5):
        numbers.append(i)
        alpha_corr(cnt + 1)
        numbers.pop()

    return

alpha_corr(0)
print(result)