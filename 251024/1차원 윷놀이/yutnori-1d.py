N, M, K = map(int, input().split())     # 턴의 수(N), 윷놀이 판의 상태(M), 말의 수(K)
lengths = list(map(int, input().split()))

def cal_score():
    global numbers
    move = {}
    for i in range(len(numbers)):
        if move.get(numbers[i]):
            move[numbers[i]] += (lengths[i])
        else:
            move[numbers[i]] = 1 + (lengths[i])
    
    score = 0
    for key, value in move.items():
        if value >= M:
            score += 1
    return score

numbers = []
result = 0
def backtracking(depth, cnt):
    global numbers, result
    if depth == cnt:
        # print(numbers)
        result = max(result, cal_score())
        return

    for k in range(1, K + 1):
        numbers.append(k)
        backtracking(depth, cnt + 1)
        numbers.pop()
    return

backtracking(N, 0)
print(result)