N = int(input())    # 선분의 갯수

# 선분 저장
lines = []
max_r = 0
for _ in range(N):
    l, r = map(int, input().split())
    lines.append((l - 1, r - 1))
    max_r = max(max_r, r)

# 선분이 겹치는지 확인
def is_overlap(selected_lines):
    global max_r

    temp = [0] * max_r  # 중복 확인을 위한 리스트
    for line in selected_lines:
        l, r = lines[line]
        for i in range(l, r + 1):
            temp[i] += 1

    if max(temp) >= 2:
        return True
    return False

# 선분의 조합
lines_comb = []
answer = 0
def backtracking(depth, cnt):   # 선분의 갯수
    global lines_comb, answer

    if len(lines_comb) == depth:
        if not is_overlap(lines_comb):
            answer = max(answer, len(lines_comb))
        return

    for n in range(N):
        if n in lines_comb:
            return
        lines_comb.append(n)
        backtracking(depth, cnt + 1)
        lines_comb.pop()
    return

for n in range(1, N + 1):
    backtracking(n, 0)
print(answer)
