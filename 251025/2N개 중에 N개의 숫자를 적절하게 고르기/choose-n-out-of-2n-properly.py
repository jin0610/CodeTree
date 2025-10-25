import sys
INT_MAX = sys.maxsize

N = int(input())
A = list(map(int, input().split()))
# 수열 A의 합
sum_A = sum(A)

# 두 개로 나누어진 각 수열의 합의 차 구하기
def calc():
    global seq1, sum_A
    sum_seq2 = sum_A - sum(seq1)    # 전체합에서 seq1의 합을 빼면 seq2의 합이 됨
    return abs(sum_seq2 - sum(seq1))    

# 수열 나누기
seq1 = []
answer = INT_MAX
def dividing_seq(curr_idx, cnt):
    global seq1, answer

    if cnt == N:
        answer = min(answer, calc())
        return

    # 2N개의 정수로 이루어진 수열에서 N개 선택
    for i in range(curr_idx, 2 * N):
        seq1.append(A[i])
        dividing_seq(i + 1, cnt + 1)
        seq1.pop()

    return

dividing_seq(0, 0)
print(answer)