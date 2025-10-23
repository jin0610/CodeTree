K, N = map(int,input().split()) # 1 ~ K 숫자를 하나 고르는 행위를 N번 반복
selected_nums = []  # 선택된 숫자

def select_num(num):

    if len(selected_nums) == N:    # 종료조건 : 숫자를 N번 선택했을 때
        print(*selected_nums)   # 선택된 원소 출력
        return

    # 1 ~ K의 숫자가 뽑혔을 때의 경우를 탐색
    for k in range(1, K + 1):
        selected_nums.append(k)
        select_num(num + 1)
        selected_nums.pop()

    return

select_num(1)