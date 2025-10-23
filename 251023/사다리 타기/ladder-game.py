N, M = map(int, input().split())    # 세로줄 수, 가로줄 수
R, C = 0, N # 격자를 그리기 위한 열과 행 수

edges = []  # 선분
for _ in range(M):
    c, r = map(int, input().split())
    edges.append((r - 1, c - 1))
    R = max(R, r)

# 사다리 결과
def get_result(selected_edges):
    global edges
    # 선분 표시용 grid
    grid = [ 
        [0 for _ in range(C)]
        for _ in range(R)
    ]
    
    for i in selected_edges:
        r, c = edges[i]
        grid[r][c], grid[r][c + 1] = 1, 2

    result = [0] * N
    # 위에서부터 내려가며 결과 찾기
    for n in range(N):
        r, c = 0, n
        while True:
            if r >= R:
                result[c] = n + 1
                break 

            if grid[r][c] == 1:
                r, c = r + 1, c + 1
            elif grid[r][c] == 2:
                r, c = r + 1, c - 1
            else:
                r, c = r + 1, c

    return result

comb_lines = []
min_cnt = M
def backtracking(depth, cnt):
    global comb_lines, first_result, min_cnt

    if len(comb_lines) == depth:    # 종료 조건 : 선선택된 선의 개수가 depth와 같을 때
        result = get_result(comb_lines)
        if result == first_result:
            min_cnt = min(min_cnt, len(comb_lines))
        return

    for m in range(M):
        if m in comb_lines:
            return
        comb_lines.append(m)
        backtracking(depth, cnt + 1) # cnt : 현재 선택하려는 숫자가 몇번째로 선택하는 숫자인지 표시
        comb_lines.pop()

# 처음 사다리과결과
original_comb = [i for i in range(M)]# 처음사다리 결과를 얻기위한 리스트 수
first_result = get_result(original_comb)

for m in range(M):
    backtracking(m, 0)
print(min_cnt)