N = int(input()) # N자리의 수

answer = 0      # 아름다운 수의 개수
numbers = []    # N자리의 수

def is_beautiful(selected_numbers):
    number = selected_numbers[0]
    cnt = 1
    for i in range(1, N): # N자리의 수까지 있으니 범위는 N
        if selected_numbers[i] == number:   # 숫자가 같으면 나온 횟수만 세기
            cnt += 1
        else:
            if cnt % number == 0:
                number = selected_numbers[i]
                cnt = 1
            else:
                return False

    if cnt % number != 0:
        return False

    return True

def find_beautiful(num):
    global answer

    if len(numbers) == N:   # 종료 조건 : N개의 숫자를 모두 뽑았을 때
        if is_beautiful(numbers): # 선택된 숫자가 아름다운 수인지 확인
            answer += 1     # 아름다운 수이면 count
        return

    for i in range(1, 5):   # 1이상 4이하의 정수로만 이루어져 있으므로 범위는 (1, 5)
        numbers.append(i)
        find_beautiful(num + 1)
        numbers.pop()
    return

find_beautiful(1) # 1부터 시작
print(answer)