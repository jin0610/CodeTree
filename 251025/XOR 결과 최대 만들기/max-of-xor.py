N, M = map(int, input().split()) # N개의 정수, 뽑을 숫자 갯수 M
nums = list(map(int, input().split()))

answer = 0
def get_max_xor(curr_idx, cnt, curr_num):
    global answer

    if cnt == M: # M번 함수가 실행되어 숫자가 뽑혔을 경우, 함수 종료
        answer = max(answer, curr_num)
        return

    # 현재 인덱스가 N보다 크거나 같을 경우 멈추기
    # 현재 남아있는 숫자의 갯수가 부족할 경우 멈추기
    if curr_idx >= N or N - curr_idx < M - cnt:
        return
    
    for n in range(curr_idx, N):
        get_max_xor(n + 1, cnt + 1, curr_num ^ nums[n])
    # get_max_xor(curr_idx + 1, cnt + 1, curr_num ^ arr[curr_idx])
    return

get_max_xor(0, 0, 0)
print(answer)